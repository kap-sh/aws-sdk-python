"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevelFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_security_level_filter

CisSecurityLevelFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_security_level_filter.CisSecurityLevelFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisSecurityLevelFilterList) -> list:
    import aws_sdk_inspector2.types.cis_security_level_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_security_level_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CisSecurityLevelFilterList:
    import aws_sdk_inspector2.types.cis_security_level_filter

    out: CisSecurityLevelFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_security_level_filter.deserialize_json(item)
        )
    return out
