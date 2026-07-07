"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetLogDeliveryConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.log_configuration_list_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class SetLogDeliveryConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to configure logging.</p>"""
    log_configurations: "aws_sdk_cognito_identity_provider.types.log_configuration_list_type.LogConfigurationListType"
    """<p>A collection of the logging configurations for a user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetLogDeliveryConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import aws_sdk_cognito_identity_provider.types.log_configuration_list_type

    out["LogConfigurations"] = (
        aws_sdk_cognito_identity_provider.types.log_configuration_list_type.serialize_aws_json_1_1(
            value["log_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetLogDeliveryConfigurationRequest:
    out: SetLogDeliveryConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "SetLogDeliveryConfigurationRequest.user_pool_id required"
        )
    if "LogConfigurations" in data:
        import aws_sdk_cognito_identity_provider.types.log_configuration_list_type

        out["log_configurations"] = (
            aws_sdk_cognito_identity_provider.types.log_configuration_list_type.deserialize_aws_json_1_1(
                data["LogConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "SetLogDeliveryConfigurationRequest.log_configurations required"
        )
    return out
