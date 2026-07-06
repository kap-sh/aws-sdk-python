"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteIPSetResponse``."""

from typing_extensions import TypedDict


class DeleteIPSetResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIPSetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIPSetResponse:
    out: DeleteIPSetResponse = {}  # type: ignore[typeddict-item]
    return out
