"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_alias
    import aws_sdk_iotsitewise.types.entry_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.qualities
    import aws_sdk_iotsitewise.types.time_ordering
    import aws_sdk_iotsitewise.types.timestamp


class BatchGetAssetPropertyValueHistoryEntry(TypedDict):
    entry_id: "aws_sdk_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    asset_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset in which the asset property was created.</p>"""
    property_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    property_alias: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    start_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>"""
    end_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>"""
    qualities: NotRequired["aws_sdk_iotsitewise.types.qualities.Qualities"]
    """<p>The quality by which to filter asset data.</p>"""
    time_ordering: NotRequired["aws_sdk_iotsitewise.types.time_ordering.TimeOrdering"]
    """<p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistoryEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    if "start_date" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["startDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["start_date"]
        )
    if "end_date" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["endDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["end_date"]
        )
    if "qualities" in value:
        import aws_sdk_iotsitewise.types.qualities

        out["qualities"] = aws_sdk_iotsitewise.types.qualities.serialize_json(
            value["qualities"]
        )
    if "time_ordering" in value:
        import aws_sdk_iotsitewise.types.time_ordering

        out["timeOrdering"] = aws_sdk_iotsitewise.types.time_ordering.serialize_json(
            value["time_ordering"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueHistoryEntry:
    out: BatchGetAssetPropertyValueHistoryEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueHistoryEntry.entry_id required"
        )
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    if "propertyAlias" in data:
        out["property_alias"] = data["propertyAlias"]
    if "startDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["start_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["startDate"]
        )
    if "endDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["end_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["endDate"]
        )
    if "qualities" in data:
        import aws_sdk_iotsitewise.types.qualities

        out["qualities"] = aws_sdk_iotsitewise.types.qualities.deserialize_json(
            data["qualities"]
        )
    if "timeOrdering" in data:
        import aws_sdk_iotsitewise.types.time_ordering

        out["time_ordering"] = aws_sdk_iotsitewise.types.time_ordering.deserialize_json(
            data["timeOrdering"]
        )
    return out
