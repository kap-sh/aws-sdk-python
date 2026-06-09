"""Generated from Smithy shape ``com.amazonaws.iam#DeleteUserPermissionsBoundaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.user_name_type


class DeleteUserPermissionsBoundaryRequest(TypedDict):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    """<p>The name (friendly name, not ARN) of the IAM user from which you want to remove the permissions boundary.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteUserPermissionsBoundaryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> DeleteUserPermissionsBoundaryRequest:
    out: DeleteUserPermissionsBoundaryRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError(
            "DeleteUserPermissionsBoundaryRequest.user_name required"
        )
    return out
