"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarTrustAnchorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.uuid


class ScalarTrustAnchorRequest(TypedDict, closed=True):
    trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the trust anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarTrustAnchorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarTrustAnchorRequest:
    out: ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
    return out
