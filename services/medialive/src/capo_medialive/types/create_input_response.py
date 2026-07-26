"""Generated from Smithy shape ``com.amazonaws.medialive#CreateInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.input


class CreateInputResponse(TypedDict, closed=True):
    input: NotRequired["capo_medialive.types.input.Input"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputResponse) -> dict:
    out: dict = {}
    if "input" in value:
        import capo_medialive.types.input

        out["input"] = capo_medialive.types.input.serialize_json(value["input"])
    return out


def deserialize_json(data: dict) -> CreateInputResponse:
    out: CreateInputResponse = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import capo_medialive.types.input

        out["input"] = capo_medialive.types.input.deserialize_json(data["input"])
    return out
