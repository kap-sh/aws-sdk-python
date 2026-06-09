"""Generated from Smithy shape ``com.amazonaws.iam#UpdateRoleDescriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.role


class UpdateRoleDescriptionResponse(TypedDict):
    role: NotRequired["aws_sdk_iam.types.role.Role"]
    """<p>A structure that contains details about the modified role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateRoleDescriptionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "role" in value:
        import aws_sdk_iam.types.role

        aws_sdk_iam.types.role.serialize_query(value["role"], pairs, f"{prefix}.Role")


def deserialize_query(el: Element) -> UpdateRoleDescriptionResponse:
    out: UpdateRoleDescriptionResponse = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        import aws_sdk_iam.types.role

        out["role"] = aws_sdk_iam.types.role.deserialize_query(child_role)
    return out
