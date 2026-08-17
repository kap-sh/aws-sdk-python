"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderTelemetryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_logging_config


class CapacityProviderTelemetryConfig(TypedDict, closed=True):
    logging_config: NotRequired[
        "capo_lambda.types.capacity_provider_logging_config.CapacityProviderLoggingConfig"
    ]
    """<p>The capacity provider's Amazon CloudWatch Logs configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderTelemetryConfig) -> dict:
    out: dict = {}
    if "logging_config" in value:
        import capo_lambda.types.capacity_provider_logging_config

        out["LoggingConfig"] = (
            capo_lambda.types.capacity_provider_logging_config.serialize_json(
                value["logging_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityProviderTelemetryConfig:
    out: CapacityProviderTelemetryConfig = {}  # type: ignore[typeddict-item]
    if data.get("LoggingConfig") is not None:
        import capo_lambda.types.capacity_provider_logging_config

        out["logging_config"] = (
            capo_lambda.types.capacity_provider_logging_config.deserialize_json(
                data["LoggingConfig"]
            )
        )
    return out
