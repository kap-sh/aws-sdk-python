"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit256

ComplianceResourceTypes: TypeAlias = list[
    "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceResourceTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ComplianceResourceTypes:
    return list(data)
