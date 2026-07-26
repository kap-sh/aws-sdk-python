"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.compliance_execution_id
    import capo_ssm.types.compliance_execution_type
    import capo_ssm.types.date_time


class ComplianceExecutionSummary(TypedDict, closed=True):
    execution_time: "capo_ssm.types.date_time.DateTime"
    """<p>The time the execution ran as a datetime object that is saved in the following format: <code>yyyy-MM-dd'T'HH:mm:ss'Z'</code> </p> <important> <p>For State Manager associations, this timestamp represents when the compliance status was captured and reported by the Systems Manager service, not when the underlying association was actually executed on the managed node. To track actual association execution times, use the <a>DescribeAssociationExecutionTargets</a> command or check the association execution history in the Systems Manager console.</p> </important>"""
    execution_id: NotRequired[
        "capo_ssm.types.compliance_execution_id.ComplianceExecutionId"
    ]
    """<p>An ID created by the system when <code>PutComplianceItems</code> was called. For example, <code>CommandID</code> is a valid execution ID. You can use this ID in subsequent calls.</p>"""
    execution_type: NotRequired[
        "capo_ssm.types.compliance_execution_type.ComplianceExecutionType"
    ]
    """<p>The type of execution. For example, <code>Command</code> is a valid execution type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceExecutionSummary) -> dict:
    out: dict = {}
    import capo_ssm.types.date_time

    out["ExecutionTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
        value["execution_time"]
    )
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "execution_type" in value:
        out["ExecutionType"] = value["execution_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceExecutionSummary:
    out: ComplianceExecutionSummary = {}  # type: ignore[typeddict-item]
    if "ExecutionTime" in data:
        import capo_ssm.types.date_time

        out["execution_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionTime"]
        )
    else:
        raise DeserializationError("ComplianceExecutionSummary.execution_time required")
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "ExecutionType" in data:
        out["execution_type"] = data["ExecutionType"]
    return out
