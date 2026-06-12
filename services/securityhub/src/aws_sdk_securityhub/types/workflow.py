"""Generated from Smithy shape ``com.amazonaws.securityhub#Workflow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.workflow_status


class Workflow(TypedDict):
    status: NotRequired["aws_sdk_securityhub.types.workflow_status.WorkflowStatus"]
    """<p>The status of the investigation into the finding. The workflow status is specific to an individual finding. It does not affect the generation of new findings. For example, setting the workflow status to <code>SUPPRESSED</code> or <code>RESOLVED</code> does not prevent a new finding for the same issue.</p> <p>The allowed values are the following.</p> <ul> <li> <p> <code>NEW</code> - The initial state of a finding, before it is reviewed.</p> <p>Security Hub CSPM also resets the workflow status from <code>NOTIFIED</code> or <code>RESOLVED</code> to <code>NEW</code> in the following cases:</p> <ul> <li> <p> <code>RecordState</code> changes from <code>ARCHIVED</code> to <code>ACTIVE</code>.</p> </li> <li> <p> <code>ComplianceStatus</code> changes from <code>PASSED</code> to either <code>WARNING</code>, <code>FAILED</code>, or <code>NOT_AVAILABLE</code>.</p> </li> </ul> </li> <li> <p> <code>NOTIFIED</code> - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.</p> </li> <li> <p> <code>SUPPRESSED</code> - Indicates that you reviewed the finding and don't believe that any action is needed. The finding is no longer updated.</p> </li> <li> <p> <code>RESOLVED</code> - The finding was reviewed and remediated and is now considered resolved. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Workflow) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_securityhub.types.workflow_status

        out["Status"] = aws_sdk_securityhub.types.workflow_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> Workflow:
    out: Workflow = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_securityhub.types.workflow_status

        out["status"] = aws_sdk_securityhub.types.workflow_status.deserialize_json(
            data["Status"]
        )
    return out
