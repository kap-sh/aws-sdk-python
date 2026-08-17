"""Generated from Smithy shape ``com.amazonaws.lambda#ListLayerVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.layer_versions_list
    import capo_lambda.types.string


class ListLayerVersionsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>A pagination token returned when the response doesn't contain all versions.</p>"""
    layer_versions: NotRequired[
        "capo_lambda.types.layer_versions_list.LayerVersionsList"
    ]
    """<p>A list of versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayerVersionsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "layer_versions" in value:
        import capo_lambda.types.layer_versions_list

        out["LayerVersions"] = capo_lambda.types.layer_versions_list.serialize_json(
            value["layer_versions"]
        )
    return out


def deserialize_json(data: dict) -> ListLayerVersionsResponse:
    out: ListLayerVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("LayerVersions") is not None:
        import capo_lambda.types.layer_versions_list

        out["layer_versions"] = capo_lambda.types.layer_versions_list.deserialize_json(
            data["LayerVersions"]
        )
    return out
