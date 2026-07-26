"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_flow_name
    import capo_connect.types.contact_flow_state
    import capo_connect.types.contact_flow_status
    import capo_connect.types.contact_flow_type


class ContactFlowSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    name: NotRequired["capo_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the flow.</p>"""
    contact_flow_type: NotRequired[
        "capo_connect.types.contact_flow_type.ContactFlowType"
    ]
    """<p>The type of flow.</p>"""
    contact_flow_state: NotRequired[
        "capo_connect.types.contact_flow_state.ContactFlowState"
    ]
    """<p>The type of flow.</p>"""
    contact_flow_status: NotRequired[
        "capo_connect.types.contact_flow_status.ContactFlowStatus"
    ]
    """<p>The status of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "contact_flow_type" in value:
        import capo_connect.types.contact_flow_type

        out["ContactFlowType"] = capo_connect.types.contact_flow_type.serialize_json(
            value["contact_flow_type"]
        )
    if "contact_flow_state" in value:
        import capo_connect.types.contact_flow_state

        out["ContactFlowState"] = capo_connect.types.contact_flow_state.serialize_json(
            value["contact_flow_state"]
        )
    if "contact_flow_status" in value:
        import capo_connect.types.contact_flow_status

        out["ContactFlowStatus"] = (
            capo_connect.types.contact_flow_status.serialize_json(
                value["contact_flow_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowSummary:
    out: ContactFlowSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ContactFlowType" in data:
        import capo_connect.types.contact_flow_type

        out["contact_flow_type"] = (
            capo_connect.types.contact_flow_type.deserialize_json(
                data["ContactFlowType"]
            )
        )
    if "ContactFlowState" in data:
        import capo_connect.types.contact_flow_state

        out["contact_flow_state"] = (
            capo_connect.types.contact_flow_state.deserialize_json(
                data["ContactFlowState"]
            )
        )
    if "ContactFlowStatus" in data:
        import capo_connect.types.contact_flow_status

        out["contact_flow_status"] = (
            capo_connect.types.contact_flow_status.deserialize_json(
                data["ContactFlowStatus"]
            )
        )
    return out
