"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingSchemaListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_id
    import capo_iot_managed_integrations.types.endpoint_id
    import capo_iot_managed_integrations.types.validation_schema


class ManagedThingSchemaListItem(TypedDict, closed=True):
    endpoint_id: NotRequired[
        "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
    ]
    """<p>The id of the endpoint for a managed thing.</p>"""
    capability_id: NotRequired[
        "capo_iot_managed_integrations.types.capability_id.CapabilityId"
    ]
    """<p>The id of the capability for a managed thing.</p>"""
    schema: NotRequired[
        "capo_iot_managed_integrations.types.validation_schema.ValidationSchema"
    ]
    """<p>The validation schema for one schema item associated with a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingSchemaListItem) -> dict:
    out: dict = {}
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "capability_id" in value:
        out["CapabilityId"] = value["capability_id"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> ManagedThingSchemaListItem:
    out: ManagedThingSchemaListItem = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "CapabilityId" in data:
        out["capability_id"] = data["CapabilityId"]
    if "Schema" in data:
        out["schema"] = data["Schema"]
    return out
