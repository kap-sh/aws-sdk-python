"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SkippedIPRangeListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.string_type

SkippedIPRangeListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.string_type.StringType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SkippedIPRangeListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SkippedIPRangeListType:
    return list(data)
