"""Generated from Smithy shape ``com.amazonaws.pi#GetResourceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.feature_metadata_map
    import capo_pi.types.string


class GetResourceMetadataResponse(TypedDict, closed=True):
    identifier: NotRequired["capo_pi.types.string.String"]
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>. </p>"""
    features: NotRequired["capo_pi.types.feature_metadata_map.FeatureMetadataMap"]
    """<p>The metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceMetadataResponse) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "features" in value:
        import capo_pi.types.feature_metadata_map

        out["Features"] = capo_pi.types.feature_metadata_map.serialize_aws_json_1_1(
            value["features"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceMetadataResponse:
    out: GetResourceMetadataResponse = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "Features" in data:
        import capo_pi.types.feature_metadata_map

        out["features"] = capo_pi.types.feature_metadata_map.deserialize_aws_json_1_1(
            data["Features"]
        )
    return out
