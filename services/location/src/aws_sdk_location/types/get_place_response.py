"""Generated from Smithy shape ``com.amazonaws.location#GetPlaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.place


class GetPlaceResponse(TypedDict):
    place: "aws_sdk_location.types.place.Place"
    """<p>Details about the result, such as its address and position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.place

    out["Place"] = aws_sdk_location.types.place.serialize_json(value["place"])
    return out


def deserialize_json(data: dict) -> GetPlaceResponse:
    out: GetPlaceResponse = {}  # type: ignore[typeddict-item]
    if "Place" in data:
        import aws_sdk_location.types.place

        out["place"] = aws_sdk_location.types.place.deserialize_json(data["Place"])
    else:
        raise DeserializationError("GetPlaceResponse.place required")
    return out
