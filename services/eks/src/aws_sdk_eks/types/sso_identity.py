"""Generated from Smithy shape ``com.amazonaws.eks#SsoIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.sso_identity_type
    import aws_sdk_eks.types.string


class SsoIdentity(TypedDict, closed=True):
    id: "aws_sdk_eks.types.string.String"
    """<p>The unique identifier of the IAM Identity CenterIAM; Identity Center user or group.</p>"""
    type: "aws_sdk_eks.types.sso_identity_type.SsoIdentityType"
    """<p>The type of identity. Valid values are <code>SSO_USER</code> or <code>SSO_GROUP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsoIdentity) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_eks.types.sso_identity_type

    out["type"] = aws_sdk_eks.types.sso_identity_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SsoIdentity:
    out: SsoIdentity = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SsoIdentity.id required")
    if "type" in data:
        import aws_sdk_eks.types.sso_identity_type

        out["type"] = aws_sdk_eks.types.sso_identity_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("SsoIdentity.type required")
    return out
