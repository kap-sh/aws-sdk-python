"""Generated from Smithy shape ``com.amazonaws.appmesh#CertificateAuthorityArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.arn

CertificateAuthorityArns: TypeAlias = list["aws_sdk_app_mesh.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityArns) -> list:
    return list(value)


def deserialize_json(data: list) -> CertificateAuthorityArns:
    return list(data)
