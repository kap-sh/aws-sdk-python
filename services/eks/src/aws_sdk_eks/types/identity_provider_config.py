"""Generated from Smithy shape ``com.amazonaws.eks#IdentityProviderConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class IdentityProviderConfig(TypedDict):
    type: "aws_sdk_eks.types.string.String"
    """<p>The type of the identity provider configuration. The only type available is <code>oidc</code>.</p>"""
    name: "aws_sdk_eks.types.string.String"
    """<p>The name of the identity provider configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IdentityProviderConfig:
    out: IdentityProviderConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("IdentityProviderConfig.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IdentityProviderConfig.name required")
    return out
