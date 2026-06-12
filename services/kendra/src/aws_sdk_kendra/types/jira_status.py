"""Generated from Smithy shape ``com.amazonaws.kendra#JiraStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.string

JiraStatus: TypeAlias = list["aws_sdk_kendra.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JiraStatus) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> JiraStatus:
    return list(data)
