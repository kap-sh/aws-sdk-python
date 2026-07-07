"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255


class DeleteWorkflowRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    workflow_id: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>Unique identifier for the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRequest:
    out: DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
