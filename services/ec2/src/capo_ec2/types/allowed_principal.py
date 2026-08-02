"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.principal_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class AllowedPrincipal(TypedDict, closed=True):
    principal_type: NotRequired["capo_ec2.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""
    service_permission_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service permission.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    service_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllowedPrincipal, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "principal_type" in value:
        import capo_ec2.types.principal_type

        capo_ec2.types.principal_type.serialize_ec2_query(
            value["principal_type"], pairs, f"{key_prefix}PrincipalType"
        )
    if "principal" in value:
        pairs.append((f"{key_prefix}Principal", str(value["principal"])))
    if "service_permission_id" in value:
        pairs.append(
            (f"{key_prefix}ServicePermissionId", str(value["service_permission_id"]))
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))


def deserialize_ec2_query(el: Element) -> AllowedPrincipal:
    out: AllowedPrincipal = {}  # type: ignore[typeddict-item]
    child_principal_type = el.find("PrincipalType")
    if child_principal_type is not None:
        import capo_ec2.types.principal_type

        out["principal_type"] = capo_ec2.types.principal_type.deserialize_ec2_query(
            child_principal_type
        )
    child_principal = el.find("Principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    child_service_permission_id = el.find("ServicePermissionId")
    if child_service_permission_id is not None:
        out["service_permission_id"] = str(child_service_permission_id.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    return out
