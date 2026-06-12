"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CertificateThumbprintList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.certificate_thumbprint

CertificateThumbprintList: TypeAlias = list["aws_sdk_workspaces_web.types.certificate_thumbprint.CertificateThumbprint"]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateThumbprintList) -> list:
    return list(value)


def deserialize_json(data: list) -> CertificateThumbprintList:
    return list(data)