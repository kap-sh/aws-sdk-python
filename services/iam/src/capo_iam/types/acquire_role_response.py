"""Generated from Smithy shape ``com.amazonaws.iam#AcquireRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.role


class AcquireRoleResponse(TypedDict, closed=True):
    role: "capo_iam.types.role.Role"
    """<p>A structure that contains details about the IAM role that was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AcquireRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.role

    capo_iam.types.role.serialize_query(value["role"], pairs, f"{key_prefix}Role")


def deserialize_query(el: Element) -> AcquireRoleResponse:
    out: AcquireRoleResponse = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        import capo_iam.types.role

        out["role"] = capo_iam.types.role.deserialize_query(child_role)
    else:
        raise DeserializationError("AcquireRoleResponse.role required")
    return out
