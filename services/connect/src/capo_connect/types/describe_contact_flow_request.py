"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.instance_id


class DescribeContactFlowRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeContactFlowRequest:
    out: DescribeContactFlowRequest = {}  # type: ignore[typeddict-item]
    return out
