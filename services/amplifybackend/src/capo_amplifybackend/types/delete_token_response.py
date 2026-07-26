"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeleteTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__boolean


class DeleteTokenResponse(TypedDict, closed=True):
    is_success: NotRequired["capo_amplifybackend.types.__boolean.__boolean"]
    """<p>Indicates whether the request succeeded or failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTokenResponse) -> dict:
    out: dict = {}
    if "is_success" in value:
        out["isSuccess"] = value["is_success"]
    return out


def deserialize_json(data: dict) -> DeleteTokenResponse:
    out: DeleteTokenResponse = {}  # type: ignore[typeddict-item]
    if "isSuccess" in data:
        out["is_success"] = data["isSuccess"]
    return out
