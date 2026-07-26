"""Generated from Smithy shape ``com.amazonaws.secretsmanager#APIErrorListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.api_error_type

APIErrorListType: TypeAlias = list[
    "capo_secrets_manager.types.api_error_type.APIErrorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: APIErrorListType) -> list:
    import capo_secrets_manager.types.api_error_type

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.api_error_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> APIErrorListType:
    import capo_secrets_manager.types.api_error_type

    out: APIErrorListType = []
    for item in data:
        out.append(
            capo_secrets_manager.types.api_error_type.deserialize_aws_json_1_1(item)
        )
    return out
