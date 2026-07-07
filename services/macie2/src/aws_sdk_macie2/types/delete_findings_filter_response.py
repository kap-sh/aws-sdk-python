"""Generated from Smithy shape ``com.amazonaws.macie2#DeleteFindingsFilterResponse``."""

from typing_extensions import TypedDict


class DeleteFindingsFilterResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFindingsFilterResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFindingsFilterResponse:
    out: DeleteFindingsFilterResponse = {}  # type: ignore[typeddict-item]
    return out
