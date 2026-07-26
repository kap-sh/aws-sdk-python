"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListOfStringTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.string_type

ListOfStringTypes: TypeAlias = list[
    "capo_cognito_identity_provider.types.string_type.StringType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfStringTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListOfStringTypes:
    return list(data)
