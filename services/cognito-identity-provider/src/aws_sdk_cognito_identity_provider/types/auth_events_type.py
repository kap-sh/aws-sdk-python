"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthEventsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.auth_event_type

AuthEventsType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.auth_event_type.AuthEventType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthEventsType) -> list:
    import aws_sdk_cognito_identity_provider.types.auth_event_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.auth_event_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AuthEventsType:
    import aws_sdk_cognito_identity_provider.types.auth_event_type

    out: AuthEventsType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.auth_event_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
