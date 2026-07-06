"""Generated from Smithy shape ``com.amazonaws.lakeformation#RevokePermissionsResponse``."""

from typing_extensions import TypedDict


class RevokePermissionsResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RevokePermissionsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RevokePermissionsResponse:
    out: RevokePermissionsResponse = {}  # type: ignore[typeddict-item]
    return out
