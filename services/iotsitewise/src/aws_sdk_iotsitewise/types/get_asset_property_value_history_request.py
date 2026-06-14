"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetAssetPropertyValueHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_alias
    import aws_sdk_iotsitewise.types.get_asset_property_value_history_max_results
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.next_token
    import aws_sdk_iotsitewise.types.qualities
    import aws_sdk_iotsitewise.types.time_ordering
    import aws_sdk_iotsitewise.types.timestamp


class GetAssetPropertyValueHistoryRequest(TypedDict):
    asset_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset, in UUID format.</p>"""
    property_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    property_alias: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    r"""<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    start_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>"""
    end_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>"""
    qualities: NotRequired["aws_sdk_iotsitewise.types.qualities.Qualities"]
    """<p>The quality by which to filter asset data.</p>"""
    time_ordering: NotRequired["aws_sdk_iotsitewise.types.time_ordering.TimeOrdering"]
    """<p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iotsitewise.types.get_asset_property_value_history_max_results.GetAssetPropertyValueHistoryMaxResults"
    ]
    """<p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetPropertyValueHistoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetPropertyValueHistoryRequest:
    out: GetAssetPropertyValueHistoryRequest = {}  # type: ignore[typeddict-item]
    return out
