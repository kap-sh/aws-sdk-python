"""Generated from Smithy shape ``com.amazonaws.appstream#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.string

StringList: TypeAlias = list["capo_appstream.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StringList:
    return list(data)
