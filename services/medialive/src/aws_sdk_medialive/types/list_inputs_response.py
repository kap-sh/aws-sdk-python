"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input
    import aws_sdk_medialive.types.__string


class ListInputsResponse(TypedDict):
    inputs: NotRequired["aws_sdk_medialive.types.__list_of_input.__listOfInput"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputsResponse) -> dict:
    out: dict = {}
    if "inputs" in value:
        import aws_sdk_medialive.types.__list_of_input

        out["inputs"] = aws_sdk_medialive.types.__list_of_input.serialize_json(
            value["inputs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputsResponse:
    out: ListInputsResponse = {}  # type: ignore[typeddict-item]
    if "inputs" in data:
        import aws_sdk_medialive.types.__list_of_input

        out["inputs"] = aws_sdk_medialive.types.__list_of_input.deserialize_json(
            data["inputs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
