"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompromisedCredentialsActionsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.compromised_credentials_event_action_type


class CompromisedCredentialsActionsType(TypedDict, closed=True):
    event_action: "aws_sdk_cognito_identity_provider.types.compromised_credentials_event_action_type.CompromisedCredentialsEventActionType"
    """<p>The action that Amazon Cognito takes when it detects compromised credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompromisedCredentialsActionsType) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.compromised_credentials_event_action_type

    out["EventAction"] = (
        aws_sdk_cognito_identity_provider.types.compromised_credentials_event_action_type.serialize_aws_json_1_1(
            value["event_action"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompromisedCredentialsActionsType:
    out: CompromisedCredentialsActionsType = {}  # type: ignore[typeddict-item]
    if "EventAction" in data:
        import aws_sdk_cognito_identity_provider.types.compromised_credentials_event_action_type

        out["event_action"] = (
            aws_sdk_cognito_identity_provider.types.compromised_credentials_event_action_type.deserialize_aws_json_1_1(
                data["EventAction"]
            )
        )
    else:
        raise DeserializationError(
            "CompromisedCredentialsActionsType.event_action required"
        )
    return out
