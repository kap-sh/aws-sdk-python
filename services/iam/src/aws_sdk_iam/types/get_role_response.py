"""Generated from Smithy shape ``com.amazonaws.iam#GetRoleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.role


class GetRoleResponse(TypedDict):
    role: "aws_sdk_iam.types.role.Role"
    """<p>A structure containing details about the IAM role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.role

    aws_sdk_iam.types.role.serialize_query(value["role"], pairs, f"{prefix}.Role")


def deserialize_query(el: Element) -> GetRoleResponse:
    out: GetRoleResponse = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        import aws_sdk_iam.types.role

        out["role"] = aws_sdk_iam.types.role.deserialize_query(child_role)
    else:
        raise DeserializationError("GetRoleResponse.role required")
    return out
