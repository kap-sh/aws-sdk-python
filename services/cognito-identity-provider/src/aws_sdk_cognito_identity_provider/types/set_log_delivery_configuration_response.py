"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetLogDeliveryConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type


class SetLogDeliveryConfigurationResponse(TypedDict):
    log_delivery_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type.LogDeliveryConfigurationType"
    ]
    """<p>The logging configuration that you applied to the requested user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetLogDeliveryConfigurationResponse) -> dict:
    out: dict = {}
    if "log_delivery_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type

        out["LogDeliveryConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type.serialize_aws_json_1_1(
                value["log_delivery_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetLogDeliveryConfigurationResponse:
    out: SetLogDeliveryConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LogDeliveryConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type

        out["log_delivery_configuration"] = (
            aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type.deserialize_aws_json_1_1(
                data["LogDeliveryConfiguration"]
            )
        )
    return out
