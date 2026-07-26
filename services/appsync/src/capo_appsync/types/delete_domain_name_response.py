"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteDomainNameResponse``."""

from typing_extensions import TypedDict


class DeleteDomainNameResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainNameResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainNameResponse:
    out: DeleteDomainNameResponse = {}  # type: ignore[typeddict-item]
    return out
