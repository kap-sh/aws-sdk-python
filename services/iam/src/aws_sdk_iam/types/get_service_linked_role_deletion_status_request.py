"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLinkedRoleDeletionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.deletion_task_id_type


class GetServiceLinkedRoleDeletionStatusRequest(TypedDict, closed=True):
    deletion_task_id: "aws_sdk_iam.types.deletion_task_id_type.DeletionTaskIdType"
    r"""<p>The deletion task identifier. This identifier is returned by the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html\">DeleteServiceLinkedRole</a> operation in the format <code>task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid></code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetServiceLinkedRoleDeletionStatusRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.DeletionTaskId", str(value["deletion_task_id"])))


def deserialize_query(el: Element) -> GetServiceLinkedRoleDeletionStatusRequest:
    out: GetServiceLinkedRoleDeletionStatusRequest = {}  # type: ignore[typeddict-item]
    child_deletion_task_id = el.find("DeletionTaskId")
    if child_deletion_task_id is not None:
        out["deletion_task_id"] = str(child_deletion_task_id.text or "")
    else:
        raise DeserializationError(
            "GetServiceLinkedRoleDeletionStatusRequest.deletion_task_id required"
        )
    return out
