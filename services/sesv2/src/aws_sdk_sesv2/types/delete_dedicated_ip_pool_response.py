"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteDedicatedIpPoolResponse``."""

from typing_extensions import TypedDict


class DeleteDedicatedIpPoolResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDedicatedIpPoolResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDedicatedIpPoolResponse:
    out: DeleteDedicatedIpPoolResponse = {}  # type: ignore[typeddict-item]
    return out
