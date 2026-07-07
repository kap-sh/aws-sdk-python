"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetRuntimeLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetRuntimeLogConfigurationRequest(TypedDict, closed=True):
    managed_thing_id: (
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The id for a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeLogConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuntimeLogConfigurationRequest:
    out: GetRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
