"""Generated from Smithy shape ``com.amazonaws.eks#SsoIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.sso_identity

SsoIdentityList: TypeAlias = list["capo_eks.types.sso_identity.SsoIdentity"]


# --- restJson1 ser/de ---
def serialize_json(value: SsoIdentityList) -> list:
    import capo_eks.types.sso_identity

    out: list = []
    for item in value:
        out.append(capo_eks.types.sso_identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> SsoIdentityList:
    import capo_eks.types.sso_identity

    out: SsoIdentityList = []
    for item in data:
        out.append(capo_eks.types.sso_identity.deserialize_json(item))
    return out
