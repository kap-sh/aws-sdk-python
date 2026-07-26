"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthEventsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.auth_event_type

AuthEventsType: TypeAlias = list[
    "capo_cognito_identity_provider.types.auth_event_type.AuthEventType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthEventsType) -> list:
    import capo_cognito_identity_provider.types.auth_event_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.auth_event_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AuthEventsType:
    import capo_cognito_identity_provider.types.auth_event_type

    out: AuthEventsType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.auth_event_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
