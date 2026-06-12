"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ResetRuntimeLogConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class ResetRuntimeLogConfigurationRequest(TypedDict):
    managed_thing_id: (
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The id of a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetRuntimeLogConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResetRuntimeLogConfigurationRequest:
    out: ResetRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
