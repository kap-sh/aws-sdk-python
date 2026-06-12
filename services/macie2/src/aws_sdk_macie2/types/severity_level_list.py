"""Generated from Smithy shape ``com.amazonaws.macie2#SeverityLevelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.severity_level

SeverityLevelList: TypeAlias = list["aws_sdk_macie2.types.severity_level.SeverityLevel"]


# --- restJson1 ser/de ---
def serialize_json(value: SeverityLevelList) -> list:
    import aws_sdk_macie2.types.severity_level

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.severity_level.serialize_json(item))
    return out


def deserialize_json(data: list) -> SeverityLevelList:
    import aws_sdk_macie2.types.severity_level

    out: SeverityLevelList = []
    for item in data:
        out.append(aws_sdk_macie2.types.severity_level.deserialize_json(item))
    return out
