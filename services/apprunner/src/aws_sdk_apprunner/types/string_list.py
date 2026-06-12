"""Generated from Smithy shape ``com.amazonaws.apprunner#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.string

StringList: TypeAlias = list["aws_sdk_apprunner.types.string.String"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringList:
    return list(data)
