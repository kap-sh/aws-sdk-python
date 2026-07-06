"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompromisedCredentialsRiskConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.compromised_credentials_actions_type
    import aws_sdk_cognito_identity_provider.types.event_filters_type


class CompromisedCredentialsRiskConfigurationType(TypedDict, closed=True):
    event_filter: NotRequired[
        "aws_sdk_cognito_identity_provider.types.event_filters_type.EventFiltersType"
    ]
    """<p>Settings for the sign-in activity where you want to configure compromised-credentials actions. Defaults to all events.</p>"""
    actions: "aws_sdk_cognito_identity_provider.types.compromised_credentials_actions_type.CompromisedCredentialsActionsType"
    """<p>Settings for the actions that you want your user pool to take when Amazon Cognito detects compromised credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompromisedCredentialsRiskConfigurationType) -> dict:
    out: dict = {}
    if "event_filter" in value:
        import aws_sdk_cognito_identity_provider.types.event_filters_type

        out["EventFilter"] = (
            aws_sdk_cognito_identity_provider.types.event_filters_type.serialize_aws_json_1_1(
                value["event_filter"]
            )
        )
    import aws_sdk_cognito_identity_provider.types.compromised_credentials_actions_type

    out["Actions"] = (
        aws_sdk_cognito_identity_provider.types.compromised_credentials_actions_type.serialize_aws_json_1_1(
            value["actions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompromisedCredentialsRiskConfigurationType:
    out: CompromisedCredentialsRiskConfigurationType = {}  # type: ignore[typeddict-item]
    if "EventFilter" in data:
        import aws_sdk_cognito_identity_provider.types.event_filters_type

        out["event_filter"] = (
            aws_sdk_cognito_identity_provider.types.event_filters_type.deserialize_aws_json_1_1(
                data["EventFilter"]
            )
        )
    if "Actions" in data:
        import aws_sdk_cognito_identity_provider.types.compromised_credentials_actions_type

        out["actions"] = (
            aws_sdk_cognito_identity_provider.types.compromised_credentials_actions_type.deserialize_aws_json_1_1(
                data["Actions"]
            )
        )
    else:
        raise DeserializationError(
            "CompromisedCredentialsRiskConfigurationType.actions required"
        )
    return out
