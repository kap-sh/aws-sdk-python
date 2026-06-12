"""Generated from Smithy shape ``com.amazonaws.kendra#Project``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.string

Project: TypeAlias = list["aws_sdk_kendra.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Project) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Project:
    return list(data)
