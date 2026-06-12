"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateIntegrationWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.uuid


class CreateIntegrationWorkflowResponse(TypedDict):
    workflow_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>Unique identifier for the workflow.</p>"""
    message: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>A message indicating create request was received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationWorkflowResponse:
    out: CreateIntegrationWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError(
            "CreateIntegrationWorkflowResponse.workflow_id required"
        )
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("CreateIntegrationWorkflowResponse.message required")
    return out
