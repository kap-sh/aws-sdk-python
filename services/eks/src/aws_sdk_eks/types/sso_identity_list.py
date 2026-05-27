"""Generated from Smithy shape ``com.amazonaws.eks#SsoIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.sso_identity

SsoIdentityList: TypeAlias = list["aws_sdk_eks.types.sso_identity.SsoIdentity"]


# --- restJson1 ser/de ---
def serialize_json(value: SsoIdentityList) -> list:
    import aws_sdk_eks.types.sso_identity

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.sso_identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> SsoIdentityList:
    import aws_sdk_eks.types.sso_identity

    out: SsoIdentityList = []
    for item in data:
        out.append(aws_sdk_eks.types.sso_identity.deserialize_json(item))
    return out
