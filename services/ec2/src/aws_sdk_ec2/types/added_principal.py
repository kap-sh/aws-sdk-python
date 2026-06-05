"""Generated from Smithy shape ``com.amazonaws.ec2#AddedPrincipal``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.principal_type
    import aws_sdk_ec2.types.string


class AddedPrincipal(TypedDict):
    principal_type: NotRequired["aws_sdk_ec2.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""
    service_permission_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service permission.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddedPrincipal, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "principal_type" in value:
        import aws_sdk_ec2.types.principal_type

        aws_sdk_ec2.types.principal_type.serialize_ec2_query(
            value["principal_type"], pairs, f"{prefix}.PrincipalType"
        )
    if "principal" in value:
        pairs.append((f"{prefix}.Principal", str(value["principal"])))
    if "service_permission_id" in value:
        pairs.append(
            (f"{prefix}.ServicePermissionId", str(value["service_permission_id"]))
        )
    if "service_id" in value:
        pairs.append((f"{prefix}.ServiceId", str(value["service_id"])))


def deserialize_ec2_query(el: Element) -> AddedPrincipal:
    out: AddedPrincipal = {}  # type: ignore[typeddict-item]
    child_principal_type = el.find("PrincipalType")
    if child_principal_type is not None:
        import aws_sdk_ec2.types.principal_type

        out["principal_type"] = aws_sdk_ec2.types.principal_type.deserialize_ec2_query(
            child_principal_type
        )
    child_principal = el.find("Principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    child_service_permission_id = el.find("ServicePermissionId")
    if child_service_permission_id is not None:
        out["service_permission_id"] = str(child_service_permission_id.text or "")
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    return out
