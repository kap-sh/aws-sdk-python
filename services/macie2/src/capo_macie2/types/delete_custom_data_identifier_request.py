"""Generated from Smithy shape ``com.amazonaws.macie2#DeleteCustomDataIdentifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class DeleteCustomDataIdentifierRequest(TypedDict, closed=True):
    id: "capo_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomDataIdentifierRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomDataIdentifierRequest:
    out: DeleteCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
    return out
