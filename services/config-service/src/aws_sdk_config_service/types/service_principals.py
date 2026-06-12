"""Generated from Smithy shape ``com.amazonaws.configservice#ServicePrincipals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit128

ServicePrincipals: TypeAlias = list[
    "aws_sdk_config_service.types.string_with_char_limit128.StringWithCharLimit128"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServicePrincipals) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ServicePrincipals:
    return list(data)
