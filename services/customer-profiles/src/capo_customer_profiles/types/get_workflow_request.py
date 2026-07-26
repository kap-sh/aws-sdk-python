"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.uuid


class GetWorkflowRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    workflow_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>Unique identifier for the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowRequest:
    out: GetWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
