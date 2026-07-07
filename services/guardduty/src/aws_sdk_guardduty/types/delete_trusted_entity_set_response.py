"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteTrustedEntitySetResponse``."""

from typing_extensions import TypedDict


class DeleteTrustedEntitySetResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrustedEntitySetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrustedEntitySetResponse:
    out: DeleteTrustedEntitySetResponse = {}  # type: ignore[typeddict-item]
    return out
