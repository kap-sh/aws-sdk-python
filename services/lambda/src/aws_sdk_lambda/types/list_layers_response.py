"""Generated from Smithy shape ``com.amazonaws.lambda#ListLayersResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layers_list
    import aws_sdk_lambda.types.string


class ListLayersResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>A pagination token returned when the response doesn't contain all layers.</p>"""
    layers: NotRequired["aws_sdk_lambda.types.layers_list.LayersList"]
    """<p>A list of function layers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayersResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "layers" in value:
        import aws_sdk_lambda.types.layers_list

        out["Layers"] = aws_sdk_lambda.types.layers_list.serialize_json(value["layers"])
    return out


def deserialize_json(data: dict) -> ListLayersResponse:
    out: ListLayersResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Layers" in data:
        import aws_sdk_lambda.types.layers_list

        out["layers"] = aws_sdk_lambda.types.layers_list.deserialize_json(
            data["Layers"]
        )
    return out
