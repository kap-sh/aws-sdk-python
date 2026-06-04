"""Generated from Smithy shape ``com.amazonaws.iam#CreateRoleResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.role


class CreateRoleResponse(TypedDict):
    role: "aws_sdk_iam.types.role.Role"
    """<p>A structure containing details about the new role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.role

    aws_sdk_iam.types.role.serialize_query(value["role"], pairs, f"{prefix}.Role")


def deserialize_query(el: Element) -> CreateRoleResponse:
    out: CreateRoleResponse = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        import aws_sdk_iam.types.role

        out["role"] = aws_sdk_iam.types.role.deserialize_query(child_role)
    else:
        raise DeserializationError("CreateRoleResponse.role required")
    return out
