"""Generated from Smithy shape ``com.amazonaws.connect#RecordPrimaryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.primary_values_response_set
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class RecordPrimaryValue(TypedDict, closed=True):
    record_id: NotRequired["aws_sdk_connect.types.data_table_id.DataTableId"]
    """<p>The value's record ID.</p>"""
    primary_values: NotRequired[
        "aws_sdk_connect.types.primary_values_response_set.PrimaryValuesResponseSet"
    ]
    """<p>The value's primary values.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The value's last modified time.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The value's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordPrimaryValue) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "primary_values" in value:
        import aws_sdk_connect.types.primary_values_response_set

        out["PrimaryValues"] = (
            aws_sdk_connect.types.primary_values_response_set.serialize_json(
                value["primary_values"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> RecordPrimaryValue:
    out: RecordPrimaryValue = {}  # type: ignore[typeddict-item]
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_response_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_response_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
