"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceLinkedRoleResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.deletion_task_id_type


class DeleteServiceLinkedRoleResponse(TypedDict):
    deletion_task_id: "aws_sdk_iam.types.deletion_task_id_type.DeletionTaskIdType"
    """<p>The deletion task identifier that you can use to check the status of the deletion. This identifier is returned in the format <code>task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid></code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServiceLinkedRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DeletionTaskId", str(value["deletion_task_id"])))


def deserialize_query(el: Element) -> DeleteServiceLinkedRoleResponse:
    out: DeleteServiceLinkedRoleResponse = {}  # type: ignore[typeddict-item]
    child_deletion_task_id = el.find("DeletionTaskId")
    if child_deletion_task_id is not None:
        out["deletion_task_id"] = str(child_deletion_task_id.text or "")
    else:
        raise DeserializationError(
            "DeleteServiceLinkedRoleResponse.deletion_task_id required"
        )
    return out
