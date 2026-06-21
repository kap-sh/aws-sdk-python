"""Generated from Smithy shape ``com.amazonaws.outposts#OpticalStandard``."""

from typing import Literal, TypeAlias, cast

OpticalStandard: TypeAlias = Literal[
    "OPTIC_10GBASE_SR",
    "OPTIC_10GBASE_IR",
    "OPTIC_10GBASE_LR",
    "OPTIC_40GBASE_SR",
    "OPTIC_40GBASE_ESR",
    "OPTIC_40GBASE_IR4_LR4L",
    "OPTIC_40GBASE_LR4",
    "OPTIC_100GBASE_SR4",
    "OPTIC_100GBASE_CWDM4",
    "OPTIC_100GBASE_LR4",
    "OPTIC_100G_PSM4_MSA",
    "OPTIC_1000BASE_LX",
    "OPTIC_1000BASE_SX",
]


# --- restJson1 ser/de ---
def serialize_json(value: OpticalStandard) -> str:
    return value


def deserialize_json(data: str) -> OpticalStandard:
    return cast(OpticalStandard, data)
