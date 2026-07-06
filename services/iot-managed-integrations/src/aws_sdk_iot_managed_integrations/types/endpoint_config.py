"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EndpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.lambda_config

EndpointConfig = TypedDict(
    "EndpointConfig",
    {
        "lambda": NotRequired[
            "aws_sdk_iot_managed_integrations.types.lambda_config.LambdaConfig"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfig) -> dict:
    out: dict = {}
    if "lambda" in value:
        import aws_sdk_iot_managed_integrations.types.lambda_config

        out["lambda"] = (
            aws_sdk_iot_managed_integrations.types.lambda_config.serialize_json(
                value["lambda"]
            )
        )
    return out


def deserialize_json(data: dict) -> EndpointConfig:
    out: EndpointConfig = {}  # type: ignore[typeddict-item]
    if "lambda" in data:
        import aws_sdk_iot_managed_integrations.types.lambda_config

        out["lambda"] = (
            aws_sdk_iot_managed_integrations.types.lambda_config.deserialize_json(
                data["lambda"]
            )
        )
    return out
