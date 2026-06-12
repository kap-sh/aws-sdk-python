"""Generated from Smithy shape ``com.amazonaws.swf#RegisterDomainInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.description
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.duration_in_days
    import aws_sdk_swf.types.resource_tag_list


class RegisterDomainInput(TypedDict):
    name: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>Name of the domain to register. The name must be unique in the region that the domain is registered in.</p> <p>The specified string must not start or end with whitespace. It must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    description: NotRequired["aws_sdk_swf.types.description.Description"]
    """<p>A text description of the domain.</p>"""
    workflow_execution_retention_period_in_days: (
        "aws_sdk_swf.types.duration_in_days.DurationInDays"
    )
    """<p>The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution isn't available in the results of visibility calls.</p> <p>If you pass the value <code>NONE</code> or <code>0</code> (zero), then the workflow execution history isn't retained. As soon as the workflow execution completes, the execution record and its history are deleted.</p> <p>The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-limits.html\">Amazon SWF Service Limits</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_swf.types.resource_tag_list.ResourceTagList"]
    """<p>Tags to be added when registering a domain.</p> <p>Tags may only contain unicode letters, digits, whitespace, or these symbols: <code>_ . : / = + - @</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterDomainInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["workflowExecutionRetentionPeriodInDays"] = value[
        "workflow_execution_retention_period_in_days"
    ]
    if "tags" in value:
        import aws_sdk_swf.types.resource_tag_list

        out["tags"] = aws_sdk_swf.types.resource_tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegisterDomainInput:
    out: RegisterDomainInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisterDomainInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "workflowExecutionRetentionPeriodInDays" in data:
        out["workflow_execution_retention_period_in_days"] = data[
            "workflowExecutionRetentionPeriodInDays"
        ]
    else:
        raise DeserializationError(
            "RegisterDomainInput.workflow_execution_retention_period_in_days required"
        )
    if "tags" in data:
        import aws_sdk_swf.types.resource_tag_list

        out["tags"] = aws_sdk_swf.types.resource_tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
