"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceTypesScope``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit256

ResourceTypesScope: TypeAlias = list[
    "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypesScope) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypesScope:
    return list(data)
