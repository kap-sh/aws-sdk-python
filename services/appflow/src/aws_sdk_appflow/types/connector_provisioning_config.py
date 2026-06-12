"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProvisioningConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.lambda_connector_provisioning_config

ConnectorProvisioningConfig = TypedDict(
    "ConnectorProvisioningConfig",
    {
        "lambda": NotRequired[
            "aws_sdk_appflow.types.lambda_connector_provisioning_config.LambdaConnectorProvisioningConfig"
        ],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProvisioningConfig) -> dict:
    out: dict = {}
    if "lambda" in value:
        import aws_sdk_appflow.types.lambda_connector_provisioning_config

        out["lambda"] = (
            aws_sdk_appflow.types.lambda_connector_provisioning_config.serialize_json(
                value["lambda"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProvisioningConfig:
    out: ConnectorProvisioningConfig = {}  # type: ignore[typeddict-item]
    if "lambda" in data:
        import aws_sdk_appflow.types.lambda_connector_provisioning_config

        out["lambda"] = (
            aws_sdk_appflow.types.lambda_connector_provisioning_config.deserialize_json(
                data["lambda"]
            )
        )
    return out
