"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LogDeliveryConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.log_configuration_list_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class LogDeliveryConfigurationType(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you configured logging.</p>"""
    log_configurations: "capo_cognito_identity_provider.types.log_configuration_list_type.LogConfigurationListType"
    """<p>A logging destination of a user pool. User pools can have multiple logging destinations for message-delivery and user-activity logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDeliveryConfigurationType) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import capo_cognito_identity_provider.types.log_configuration_list_type

    out["LogConfigurations"] = (
        capo_cognito_identity_provider.types.log_configuration_list_type.serialize_aws_json_1_1(
            value["log_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogDeliveryConfigurationType:
    out: LogDeliveryConfigurationType = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("LogDeliveryConfigurationType.user_pool_id required")
    if "LogConfigurations" in data:
        import capo_cognito_identity_provider.types.log_configuration_list_type

        out["log_configurations"] = (
            capo_cognito_identity_provider.types.log_configuration_list_type.deserialize_aws_json_1_1(
                data["LogConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "LogDeliveryConfigurationType.log_configurations required"
        )
    return out
