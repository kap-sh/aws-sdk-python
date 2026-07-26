"""Generated from Smithy shape ``com.amazonaws.inspector2#ImageLayerAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts


class ImageLayerAggregationResponse(TypedDict, closed=True):
    repository: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The repository the layer resides in.</p>"""
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The resource ID of the container image layer.</p>"""
    layer_hash: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The layer hash.</p>"""
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that owns the container image hosting the layer image.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that represents the count of matched findings per severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLayerAggregationResponse) -> dict:
    out: dict = {}
    out["repository"] = value["repository"]
    out["resourceId"] = value["resource_id"]
    out["layerHash"] = value["layer_hash"]
    out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> ImageLayerAggregationResponse:
    out: ImageLayerAggregationResponse = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        out["repository"] = data["repository"]
    else:
        raise DeserializationError("ImageLayerAggregationResponse.repository required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ImageLayerAggregationResponse.resource_id required")
    if "layerHash" in data:
        out["layer_hash"] = data["layerHash"]
    else:
        raise DeserializationError("ImageLayerAggregationResponse.layer_hash required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("ImageLayerAggregationResponse.account_id required")
    if "severityCounts" in data:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    return out
