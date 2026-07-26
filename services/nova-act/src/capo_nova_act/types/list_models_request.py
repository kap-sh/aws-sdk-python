"""Generated from Smithy shape ``com.amazonaws.novaact#ListModelsRequest``."""

from typing_extensions import TypedDict


class ListModelsRequest(TypedDict, closed=True):
    client_compatibility_version: "int"
    """<p>The client compatibility version to filter models by compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListModelsRequest:
    out: ListModelsRequest = {}  # type: ignore[typeddict-item]
    return out
