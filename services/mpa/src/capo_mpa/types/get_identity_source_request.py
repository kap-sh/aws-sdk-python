"""Generated from Smithy shape ``com.amazonaws.mpa#GetIdentitySourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.string


class GetIdentitySourceRequest(TypedDict, closed=True):
    identity_source_arn: "capo_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the identity source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentitySourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdentitySourceRequest:
    out: GetIdentitySourceRequest = {}  # type: ignore[typeddict-item]
    return out
