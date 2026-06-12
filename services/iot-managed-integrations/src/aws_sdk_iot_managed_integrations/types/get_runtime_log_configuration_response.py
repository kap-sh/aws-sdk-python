"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetRuntimeLogConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.runtime_log_configurations


class GetRuntimeLogConfigurationResponse(TypedDict):
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id for a managed thing.</p>"""
    runtime_log_configurations: NotRequired[
        "aws_sdk_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations"
    ]
    """<p>The runtime log configuration for a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeLogConfigurationResponse) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "runtime_log_configurations" in value:
        import aws_sdk_iot_managed_integrations.types.runtime_log_configurations

        out["RuntimeLogConfigurations"] = (
            aws_sdk_iot_managed_integrations.types.runtime_log_configurations.serialize_json(
                value["runtime_log_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRuntimeLogConfigurationResponse:
    out: GetRuntimeLogConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "RuntimeLogConfigurations" in data:
        import aws_sdk_iot_managed_integrations.types.runtime_log_configurations

        out["runtime_log_configurations"] = (
            aws_sdk_iot_managed_integrations.types.runtime_log_configurations.deserialize_json(
                data["RuntimeLogConfigurations"]
            )
        )
    return out
