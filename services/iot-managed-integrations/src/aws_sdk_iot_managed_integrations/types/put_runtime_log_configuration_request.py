"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#PutRuntimeLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.runtime_log_configurations


class PutRuntimeLogConfigurationRequest(TypedDict, closed=True):
    managed_thing_id: (
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The id for a managed thing.</p>"""
    runtime_log_configurations: "aws_sdk_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations"
    """<p>The runtime log configuration for a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRuntimeLogConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.runtime_log_configurations

    out["RuntimeLogConfigurations"] = (
        aws_sdk_iot_managed_integrations.types.runtime_log_configurations.serialize_json(
            value["runtime_log_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutRuntimeLogConfigurationRequest:
    out: PutRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "RuntimeLogConfigurations" in data:
        import aws_sdk_iot_managed_integrations.types.runtime_log_configurations

        out["runtime_log_configurations"] = (
            aws_sdk_iot_managed_integrations.types.runtime_log_configurations.deserialize_json(
                data["RuntimeLogConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "PutRuntimeLogConfigurationRequest.runtime_log_configurations required"
        )
    return out
