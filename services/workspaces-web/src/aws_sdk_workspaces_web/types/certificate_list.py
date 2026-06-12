"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CertificateList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.certificate_authority_body

CertificateList: TypeAlias = list["aws_sdk_workspaces_web.types.certificate_authority_body.CertificateAuthorityBody"]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateList) -> list:
    import aws_sdk_workspaces_web.types.certificate_authority_body
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_web.types.certificate_authority_body.serialize_json(item))
    return out


def deserialize_json(data: list) -> CertificateList:
    import aws_sdk_workspaces_web.types.certificate_authority_body
    out: CertificateList = []
    for item in data:
        out.append(aws_sdk_workspaces_web.types.certificate_authority_body.deserialize_json(item))
    return out