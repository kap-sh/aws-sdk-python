"""Generated from Smithy shape ``com.amazonaws.signer#GetSigningPlatformRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.platform_id


class GetSigningPlatformRequest(TypedDict, closed=True):
    platform_id: "capo_signer.types.platform_id.PlatformId"
    """<p>The ID of the target signing platform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSigningPlatformRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSigningPlatformRequest:
    out: GetSigningPlatformRequest = {}  # type: ignore[typeddict-item]
    return out
