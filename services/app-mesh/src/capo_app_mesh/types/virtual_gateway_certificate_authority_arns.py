"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayCertificateAuthorityArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.arn

VirtualGatewayCertificateAuthorityArns: TypeAlias = list["capo_app_mesh.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayCertificateAuthorityArns) -> list:
    return list(value)


def deserialize_json(data: list) -> VirtualGatewayCertificateAuthorityArns:
    return list(data)
