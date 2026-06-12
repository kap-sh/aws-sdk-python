"""Generated from Smithy shape ``com.amazonaws.connectcases#SectionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.section

SectionsList: TypeAlias = list["aws_sdk_connectcases.types.section.Section"]


# --- restJson1 ser/de ---
def serialize_json(value: SectionsList) -> list:
    import aws_sdk_connectcases.types.section

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.section.serialize_json(item))
    return out


def deserialize_json(data: list) -> SectionsList:
    import aws_sdk_connectcases.types.section

    out: SectionsList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.section.deserialize_json(item))
    return out
