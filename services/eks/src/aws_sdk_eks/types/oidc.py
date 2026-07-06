"""Generated from Smithy shape ``com.amazonaws.eks#OIDC``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class OIDC(TypedDict, closed=True):
    issuer: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The issuer URL for the OIDC identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OIDC) -> dict:
    out: dict = {}
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    return out


def deserialize_json(data: dict) -> OIDC:
    out: OIDC = {}  # type: ignore[typeddict-item]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    return out
