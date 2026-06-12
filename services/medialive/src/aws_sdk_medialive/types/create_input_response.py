"""Generated from Smithy shape ``com.amazonaws.medialive#CreateInputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input


class CreateInputResponse(TypedDict):
    input: NotRequired["aws_sdk_medialive.types.input.Input"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputResponse) -> dict:
    out: dict = {}
    if "input" in value:
        import aws_sdk_medialive.types.input

        out["input"] = aws_sdk_medialive.types.input.serialize_json(value["input"])
    return out


def deserialize_json(data: dict) -> CreateInputResponse:
    out: CreateInputResponse = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import aws_sdk_medialive.types.input

        out["input"] = aws_sdk_medialive.types.input.deserialize_json(data["input"])
    return out
