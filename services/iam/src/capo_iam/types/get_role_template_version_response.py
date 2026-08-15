"""Generated from Smithy shape ``com.amazonaws.iam#GetRoleTemplateVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.role_template_version


class GetRoleTemplateVersionResponse(TypedDict, closed=True):
    role_template_version: "capo_iam.types.role_template_version.RoleTemplateVersion"
    """<p>A structure that contains details about the requested role template version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetRoleTemplateVersionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.role_template_version

    capo_iam.types.role_template_version.serialize_query(
        value["role_template_version"], pairs, f"{key_prefix}RoleTemplateVersion"
    )


def deserialize_query(el: Element) -> GetRoleTemplateVersionResponse:
    out: GetRoleTemplateVersionResponse = {}  # type: ignore[typeddict-item]
    child_role_template_version = el.find("RoleTemplateVersion")
    if child_role_template_version is not None:
        import capo_iam.types.role_template_version

        out["role_template_version"] = (
            capo_iam.types.role_template_version.deserialize_query(
                child_role_template_version
            )
        )
    else:
        raise DeserializationError(
            "GetRoleTemplateVersionResponse.role_template_version required"
        )
    return out
