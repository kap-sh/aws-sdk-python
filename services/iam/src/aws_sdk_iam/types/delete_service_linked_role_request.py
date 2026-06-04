"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceLinkedRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.role_name_type


class DeleteServiceLinkedRoleRequest(TypedDict):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    """<p>The name of the service-linked role to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServiceLinkedRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))


def deserialize_query(el: Element) -> DeleteServiceLinkedRoleRequest:
    out: DeleteServiceLinkedRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("DeleteServiceLinkedRoleRequest.role_name required")
    return out
