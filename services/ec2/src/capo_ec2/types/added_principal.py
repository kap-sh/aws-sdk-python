"""Generated from Smithy shape ``com.amazonaws.ec2#AddedPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.principal_type
    import capo_ec2.types.string


class AddedPrincipal(TypedDict, closed=True):
    principal_type: NotRequired["capo_ec2.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""
    service_permission_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service permission.</p>"""
    service_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddedPrincipal, pairs: list[tuple[str, str]], prefix: str
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
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))


def deserialize_ec2_query(el: Element) -> AddedPrincipal:
    out: AddedPrincipal = {}  # type: ignore[typeddict-item]
    child_principal_type = el.find("principalType")
    if child_principal_type is not None:
        import capo_ec2.types.principal_type

        out["principal_type"] = capo_ec2.types.principal_type.deserialize_ec2_query(
            child_principal_type
        )
    child_principal = el.find("principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    child_service_permission_id = el.find("servicePermissionId")
    if child_service_permission_id is not None:
        out["service_permission_id"] = str(child_service_permission_id.text or "")
    child_service_id = el.find("serviceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    return out
