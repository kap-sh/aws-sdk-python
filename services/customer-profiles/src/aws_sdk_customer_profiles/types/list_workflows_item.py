"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListWorkflowsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.status
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.workflow_type


class ListWorkflowsItem(TypedDict, closed=True):
    workflow_type: "aws_sdk_customer_profiles.types.workflow_type.WorkflowType"
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    workflow_id: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>Unique identifier for the workflow.</p>"""
    status: "aws_sdk_customer_profiles.types.status.Status"
    """<p>Status of workflow execution.</p>"""
    status_description: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>Description for workflow execution status.</p>"""
    created_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>Creation timestamp for workflow.</p>"""
    last_updated_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>Last updated timestamp for workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsItem) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.workflow_type

    out["WorkflowType"] = aws_sdk_customer_profiles.types.workflow_type.serialize_json(
        value["workflow_type"]
    )
    out["WorkflowId"] = value["workflow_id"]
    import aws_sdk_customer_profiles.types.status

    out["Status"] = aws_sdk_customer_profiles.types.status.serialize_json(
        value["status"]
    )
    out["StatusDescription"] = value["status_description"]
    import aws_sdk_customer_profiles.types.timestamp

    out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ListWorkflowsItem:
    out: ListWorkflowsItem = {}  # type: ignore[typeddict-item]
    if "WorkflowType" in data:
        import aws_sdk_customer_profiles.types.workflow_type

        out["workflow_type"] = (
            aws_sdk_customer_profiles.types.workflow_type.deserialize_json(
                data["WorkflowType"]
            )
        )
    else:
        raise DeserializationError("ListWorkflowsItem.workflow_type required")
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError("ListWorkflowsItem.workflow_id required")
    if "Status" in data:
        import aws_sdk_customer_profiles.types.status

        out["status"] = aws_sdk_customer_profiles.types.status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("ListWorkflowsItem.status required")
    if "StatusDescription" in data:
        out["status_description"] = data["StatusDescription"]
    else:
        raise DeserializationError("ListWorkflowsItem.status_description required")
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("ListWorkflowsItem.created_at required")
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("ListWorkflowsItem.last_updated_at required")
    return out
