"""Generated from Smithy shape ``com.amazonaws.swf#DeprecateWorkflowTypeInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.workflow_type


class DeprecateWorkflowTypeInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which the workflow type is registered.</p>"""
    workflow_type: "aws_sdk_swf.types.workflow_type.WorkflowType"
    """<p>The workflow type to deprecate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeprecateWorkflowTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.workflow_type

    out["workflowType"] = aws_sdk_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeprecateWorkflowTypeInput:
    out: DeprecateWorkflowTypeInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("DeprecateWorkflowTypeInput.domain required")
    if "workflowType" in data:
        import aws_sdk_swf.types.workflow_type

        out["workflow_type"] = aws_sdk_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("DeprecateWorkflowTypeInput.workflow_type required")
    return out
