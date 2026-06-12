"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.description
    import aws_sdk_swf.types.registration_status
    import aws_sdk_swf.types.timestamp
    import aws_sdk_swf.types.workflow_type


class WorkflowTypeInfo(TypedDict):
    workflow_type: "aws_sdk_swf.types.workflow_type.WorkflowType"
    """<p>The workflow type this information is about.</p>"""
    status: "aws_sdk_swf.types.registration_status.RegistrationStatus"
    """<p>The current status of the workflow type.</p>"""
    description: NotRequired["aws_sdk_swf.types.description.Description"]
    """<p>The description of the type registered through <a>RegisterWorkflowType</a>.</p>"""
    creation_date: "aws_sdk_swf.types.timestamp.Timestamp"
    """<p>The date when this type was registered.</p>"""
    deprecation_date: NotRequired["aws_sdk_swf.types.timestamp.Timestamp"]
    """<p>If the type is in deprecated state, then it is set to the date when the type was deprecated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeInfo) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.workflow_type

    out["workflowType"] = aws_sdk_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    import aws_sdk_swf.types.registration_status

    out["status"] = aws_sdk_swf.types.registration_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_swf.types.timestamp

    out["creationDate"] = aws_sdk_swf.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    if "deprecation_date" in value:
        import aws_sdk_swf.types.timestamp

        out["deprecationDate"] = aws_sdk_swf.types.timestamp.serialize_aws_json_1_0(
            value["deprecation_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowTypeInfo:
    out: WorkflowTypeInfo = {}  # type: ignore[typeddict-item]
    if "workflowType" in data:
        import aws_sdk_swf.types.workflow_type

        out["workflow_type"] = aws_sdk_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("WorkflowTypeInfo.workflow_type required")
    if "status" in data:
        import aws_sdk_swf.types.registration_status

        out["status"] = aws_sdk_swf.types.registration_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("WorkflowTypeInfo.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "creationDate" in data:
        import aws_sdk_swf.types.timestamp

        out["creation_date"] = aws_sdk_swf.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("WorkflowTypeInfo.creation_date required")
    if "deprecationDate" in data:
        import aws_sdk_swf.types.timestamp

        out["deprecation_date"] = aws_sdk_swf.types.timestamp.deserialize_aws_json_1_0(
            data["deprecationDate"]
        )
    return out
