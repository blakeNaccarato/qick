"""Generate `vhdl_ls.toml` from IPs with VHDL files."""

from pathlib import Path
from textwrap import dedent

Path("vhdl_ls.toml").write_text(
    encoding="utf-8",
    data="\n".join(
        [
            dedent("""
                standard = "2019"
                [lint]
                unused = false
                # superfluous_in_sensitivity_list = false  # ? LSP supports it, extension doesn't
                [libraries]
                common_lib.files = []
                common_lib.is_third_party = true
                unisim.files = ['C:/Xilinx/Vivado/2024.2/data/vhdl/src/unisims/unisim_VCOMP.vhd']""").strip(),
            *[
                f'{path.name}.files = ["{path.as_posix()}/src/**/*.vhd"]'
                for path in sorted(
                    [
                        p
                        for p in Path("firmware/ip").iterdir()
                        if p.is_dir()
                        # ? Not presently clear where some libs in PFB dirs come from
                        and "pfb" not in p.name
                        # ? No VHDL files in these libs
                        and p.name
                        not in {
                            "axis_reorder_iq_v1",
                            "axis_resampler_2x1_v1",
                            "axis_tmux_v1",
                            "qick_interfaces",
                            "qick_sg_translator",
                            "qick_vec2bit",
                        }
                    ]
                )
            ],
        ]
    )
    + "\n",
)
