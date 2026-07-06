"""Generated from Smithy shape ``com.amazonaws.lambda#ListLayerVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layer_versions_list
    import aws_sdk_lambda.types.string


class ListLayerVersionsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>A pagination token returned when the response doesn't contain all versions.</p>"""
    layer_versions: NotRequired[
        "aws_sdk_lambda.types.layer_versions_list.LayerVersionsList"
    ]
    """<p>A list of versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayerVersionsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "layer_versions" in value:
        import aws_sdk_lambda.types.layer_versions_list

        out["LayerVersions"] = aws_sdk_lambda.types.layer_versions_list.serialize_json(
            value["layer_versions"]
        )
    return out


def deserialize_json(data: dict) -> ListLayerVersionsResponse:
    out: ListLayerVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "LayerVersions" in data:
        import aws_sdk_lambda.types.layer_versions_list

        out["layer_versions"] = (
            aws_sdk_lambda.types.layer_versions_list.deserialize_json(
                data["LayerVersions"]
            )
        )
    return out
