"""Generated from Smithy shape ``com.amazonaws.connect#GetContactAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attributes


class GetContactAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_connect.types.attributes.Attributes"]
    """<p>Information about the attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_connect.types.attributes

        out["Attributes"] = aws_sdk_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> GetContactAttributesResponse:
    out: GetContactAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_connect.types.attributes

        out["attributes"] = aws_sdk_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    return out
