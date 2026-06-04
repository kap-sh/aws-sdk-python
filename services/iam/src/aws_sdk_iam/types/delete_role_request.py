"""Generated from Smithy shape ``com.amazonaws.iam#DeleteRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.role_name_type


class DeleteRoleRequest(TypedDict):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    """<p>The name of the role to delete.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))


def deserialize_query(el: Element) -> DeleteRoleRequest:
    out: DeleteRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("DeleteRoleRequest.role_name required")
    return out
