"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProvisioningConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.lambda_connector_provisioning_config

ConnectorProvisioningConfig = TypedDict(
    "ConnectorProvisioningConfig",
    {
        "lambda": NotRequired[
            "capo_appflow.types.lambda_connector_provisioning_config.LambdaConnectorProvisioningConfig"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProvisioningConfig) -> dict:
    out: dict = {}
    if "lambda" in value:
        import capo_appflow.types.lambda_connector_provisioning_config

        out["lambda"] = (
            capo_appflow.types.lambda_connector_provisioning_config.serialize_json(
                value["lambda"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProvisioningConfig:
    out: ConnectorProvisioningConfig = {}  # type: ignore[typeddict-item]
    if "lambda" in data:
        import capo_appflow.types.lambda_connector_provisioning_config

        out["lambda"] = (
            capo_appflow.types.lambda_connector_provisioning_config.deserialize_json(
                data["lambda"]
            )
        )
    return out
