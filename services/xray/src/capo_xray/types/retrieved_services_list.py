"""Generated from Smithy shape ``com.amazonaws.xray#RetrievedServicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.retrieved_service

RetrievedServicesList: TypeAlias = list[
    "capo_xray.types.retrieved_service.RetrievedService"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedServicesList) -> list:
    import capo_xray.types.retrieved_service

    out: list = []
    for item in value:
        out.append(capo_xray.types.retrieved_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetrievedServicesList:
    import capo_xray.types.retrieved_service

    out: RetrievedServicesList = []
    for item in data:
        out.append(capo_xray.types.retrieved_service.deserialize_json(item))
    return out
