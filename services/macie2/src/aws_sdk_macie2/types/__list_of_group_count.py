"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfGroupCount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.group_count

__listOfGroupCount: TypeAlias = list["aws_sdk_macie2.types.group_count.GroupCount"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGroupCount) -> list:
    import aws_sdk_macie2.types.group_count

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.group_count.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfGroupCount:
    import aws_sdk_macie2.types.group_count

    out: __listOfGroupCount = []
    for item in data:
        out.append(aws_sdk_macie2.types.group_count.deserialize_json(item))
    return out
