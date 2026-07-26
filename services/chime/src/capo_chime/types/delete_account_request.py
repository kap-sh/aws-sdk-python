"""Generated from Smithy shape ``com.amazonaws.chime#DeleteAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string


class DeleteAccountRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountRequest:
    out: DeleteAccountRequest = {}  # type: ignore[typeddict-item]
    return out
