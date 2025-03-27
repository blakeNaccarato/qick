"""Generate the `vhdl_ls.toml` file from IPs."""

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
                # superfluous_in_sensitivity_list = false
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
                        if p.is_dir() and "pfb" not in p.name
                    ]
                )
            ],
        ]
    )
    + "\n",
)
