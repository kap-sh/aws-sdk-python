"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetLogDeliveryConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type


class GetLogDeliveryConfigurationResponse(TypedDict, closed=True):
    log_delivery_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type.LogDeliveryConfigurationType"
    ]
    """<p>The logging configuration of the requested user pool. Includes types of logs configured and their destinations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogDeliveryConfigurationResponse) -> dict:
    out: dict = {}
    if "log_delivery_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type

        out["LogDeliveryConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type.serialize_aws_json_1_1(
                value["log_delivery_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogDeliveryConfigurationResponse:
    out: GetLogDeliveryConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LogDeliveryConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type

        out["log_delivery_configuration"] = (
            aws_sdk_cognito_identity_provider.types.log_delivery_configuration_type.deserialize_aws_json_1_1(
                data["LogDeliveryConfiguration"]
            )
        )
    return out
