"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLinkedRoleDeletionStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.deletion_task_failure_reason_type
    import aws_sdk_iam.types.deletion_task_status_type


class GetServiceLinkedRoleDeletionStatusResponse(TypedDict):
    status: "aws_sdk_iam.types.deletion_task_status_type.DeletionTaskStatusType"
    """<p>The status of the deletion.</p>"""
    reason: NotRequired[
        "aws_sdk_iam.types.deletion_task_failure_reason_type.DeletionTaskFailureReasonType"
    ]
    """<p>An object that contains details about the reason the deletion failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetServiceLinkedRoleDeletionStatusResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_iam.types.deletion_task_status_type

    aws_sdk_iam.types.deletion_task_status_type.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )
    if "reason" in value:
        import aws_sdk_iam.types.deletion_task_failure_reason_type

        aws_sdk_iam.types.deletion_task_failure_reason_type.serialize_query(
            value["reason"], pairs, f"{prefix}.Reason"
        )


def deserialize_query(el: Element) -> GetServiceLinkedRoleDeletionStatusResponse:
    out: GetServiceLinkedRoleDeletionStatusResponse = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_iam.types.deletion_task_status_type

        out["status"] = aws_sdk_iam.types.deletion_task_status_type.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError(
            "GetServiceLinkedRoleDeletionStatusResponse.status required"
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        import aws_sdk_iam.types.deletion_task_failure_reason_type

        out["reason"] = (
            aws_sdk_iam.types.deletion_task_failure_reason_type.deserialize_query(
                child_reason
            )
        )
    return out
