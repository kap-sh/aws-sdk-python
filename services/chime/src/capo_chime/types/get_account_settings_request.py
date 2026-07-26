"""Generated from Smithy shape ``com.amazonaws.chime#GetAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string


class GetAccountSettingsRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountSettingsRequest:
    out: GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
