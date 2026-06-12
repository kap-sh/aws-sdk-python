"""Generated from Smithy shape ``com.amazonaws.deadline#OutputRelativeDirectoriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string

OutputRelativeDirectoriesList: TypeAlias = list["aws_sdk_deadline.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputRelativeDirectoriesList) -> list:
    return list(value)


def deserialize_json(data: list) -> OutputRelativeDirectoriesList:
    return list(data)
