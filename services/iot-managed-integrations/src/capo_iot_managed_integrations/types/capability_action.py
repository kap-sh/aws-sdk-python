"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.action_reference
    import capo_iot_managed_integrations.types.action_trace_id
    import capo_iot_managed_integrations.types.capability_action_name
    import capo_iot_managed_integrations.types.capability_properties


class CapabilityAction(TypedDict, closed=True):
    name: "capo_iot_managed_integrations.types.capability_action_name.CapabilityActionName"
    """<p>Describe a capability action with a name.</p>"""
    ref: NotRequired[
        "capo_iot_managed_integrations.types.action_reference.ActionReference"
    ]
    """<p>Describe a capability action with an reference.</p>"""
    action_trace_id: NotRequired[
        "capo_iot_managed_integrations.types.action_trace_id.ActionTraceId"
    ]
    """<p>Describe a capability action with an <code>actionTraceId</code> for a response command.</p>"""
    parameters: NotRequired[
        "capo_iot_managed_integrations.types.capability_properties.CapabilityProperties"
    ]
    """<p>Describe a capability action with a capability property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityAction) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "ref" in value:
        out["ref"] = value["ref"]
    if "action_trace_id" in value:
        out["actionTraceId"] = value["action_trace_id"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    return out


def deserialize_json(data: dict) -> CapabilityAction:
    out: CapabilityAction = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CapabilityAction.name required")
    if "ref" in data:
        out["ref"] = data["ref"]
    if "actionTraceId" in data:
        out["action_trace_id"] = data["actionTraceId"]
    if "parameters" in data:
        out["parameters"] = data["parameters"]
    return out
