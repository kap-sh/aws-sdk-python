"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeSeriesSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property_alias
    import aws_sdk_iotsitewise.types.property_data_type
    import aws_sdk_iotsitewise.types.time_series_id
    import aws_sdk_iotsitewise.types.timestamp


class TimeSeriesSummary(TypedDict):
    asset_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset in which the asset property was created.</p>"""
    property_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    alias: NotRequired["aws_sdk_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the time series.</p>"""
    time_series_id: "aws_sdk_iotsitewise.types.time_series_id.TimeSeriesId"
    """<p>The ID of the time series.</p>"""
    data_type: "aws_sdk_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the time series.</p> <p>If you specify <code>STRUCT</code>, you must also specify <code>dataTypeSpec</code> to identify the type of the structure for this time series.</p>"""
    data_type_spec: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this time series. This parameter is required for time series that have the <code>STRUCT</code> data type.</p> <p>The options for this parameter depend on the type of the composite model in which you created the asset property that is associated with your time series. Use <code>AWS/ALARM_STATE</code> for alarm state in alarm composite models.</p>"""
    time_series_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date that the time series was created, in Unix epoch time.</p>"""
    time_series_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date that the time series was last updated, in Unix epoch time.</p>"""
    time_series_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the time series, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:time-series/${TimeSeriesId}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesSummary) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "alias" in value:
        out["alias"] = value["alias"]
    out["timeSeriesId"] = value["time_series_id"]
    import aws_sdk_iotsitewise.types.property_data_type

    out["dataType"] = aws_sdk_iotsitewise.types.property_data_type.serialize_json(
        value["data_type"]
    )
    if "data_type_spec" in value:
        out["dataTypeSpec"] = value["data_type_spec"]
    import aws_sdk_iotsitewise.types.timestamp

    out["timeSeriesCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["time_series_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["timeSeriesLastUpdateDate"] = (
        aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["time_series_last_update_date"]
        )
    )
    out["timeSeriesArn"] = value["time_series_arn"]
    return out


def deserialize_json(data: dict) -> TimeSeriesSummary:
    out: TimeSeriesSummary = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "timeSeriesId" in data:
        out["time_series_id"] = data["timeSeriesId"]
    else:
        raise DeserializationError("TimeSeriesSummary.time_series_id required")
    if "dataType" in data:
        import aws_sdk_iotsitewise.types.property_data_type

        out["data_type"] = (
            aws_sdk_iotsitewise.types.property_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("TimeSeriesSummary.data_type required")
    if "dataTypeSpec" in data:
        out["data_type_spec"] = data["dataTypeSpec"]
    if "timeSeriesCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["time_series_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["timeSeriesCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "TimeSeriesSummary.time_series_creation_date required"
        )
    if "timeSeriesLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["time_series_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["timeSeriesLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "TimeSeriesSummary.time_series_last_update_date required"
        )
    if "timeSeriesArn" in data:
        out["time_series_arn"] = data["timeSeriesArn"]
    else:
        raise DeserializationError("TimeSeriesSummary.time_series_arn required")
    return out
