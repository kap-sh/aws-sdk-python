"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.list_assets_filter
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.next_token


class ListAssetsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["aws_sdk_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""
    asset_model_id: NotRequired["aws_sdk_iotsitewise.types.custom_id.CustomID"]
    r"""<p>The ID of the asset model by which to filter the list of assets. This parameter is required if you choose <code>ALL</code> for <code>filter</code>. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    filter: NotRequired["aws_sdk_iotsitewise.types.list_assets_filter.ListAssetsFilter"]
    """<p>The filter for the requested list of assets. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all assets for a given asset model ID. The <code>assetModelId</code> parameter is required if you filter by <code>ALL</code>.</p> </li> <li> <p> <code>TOP_LEVEL</code> – The list includes only top-level assets in the asset hierarchy tree.</p> </li> </ul> <p>Default: <code>ALL</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetsRequest:
    out: ListAssetsRequest = {}  # type: ignore[typeddict-item]
    return out
