"""Generated from Smithy shape ``com.amazonaws.healthlake#DatastoreFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_name
    import aws_sdk_healthlake.types.datastore_status
    import aws_sdk_healthlake.types.timestamp


class DatastoreFilter(TypedDict, closed=True):
    datastore_name: NotRequired["aws_sdk_healthlake.types.datastore_name.DatastoreName"]
    """<p>Filter data store results by name.</p>"""
    datastore_status: NotRequired[
        "aws_sdk_healthlake.types.datastore_status.DatastoreStatus"
    ]
    """<p>Filter data store results by status.</p>"""
    created_before: NotRequired["aws_sdk_healthlake.types.timestamp.Timestamp"]
    """<p>Filter to set cutoff dates for records. All data stores created before the specified date are included in the results. </p>"""
    created_after: NotRequired["aws_sdk_healthlake.types.timestamp.Timestamp"]
    """<p>Filter to set cutoff dates for records. All data stores created after the specified date are included in the results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatastoreFilter) -> dict:
    out: dict = {}
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
    if "datastore_status" in value:
        import aws_sdk_healthlake.types.datastore_status

        out["DatastoreStatus"] = (
            aws_sdk_healthlake.types.datastore_status.serialize_aws_json_1_0(
                value["datastore_status"]
            )
        )
    if "created_before" in value:
        import aws_sdk_healthlake.types.timestamp

        out["CreatedBefore"] = (
            aws_sdk_healthlake.types.timestamp.serialize_aws_json_1_0(
                value["created_before"]
            )
        )
    if "created_after" in value:
        import aws_sdk_healthlake.types.timestamp

        out["CreatedAfter"] = aws_sdk_healthlake.types.timestamp.serialize_aws_json_1_0(
            value["created_after"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatastoreFilter:
    out: DatastoreFilter = {}  # type: ignore[typeddict-item]
    if "DatastoreName" in data:
        out["datastore_name"] = data["DatastoreName"]
    if "DatastoreStatus" in data:
        import aws_sdk_healthlake.types.datastore_status

        out["datastore_status"] = (
            aws_sdk_healthlake.types.datastore_status.deserialize_aws_json_1_0(
                data["DatastoreStatus"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_healthlake.types.timestamp

        out["created_before"] = (
            aws_sdk_healthlake.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedBefore"]
            )
        )
    if "CreatedAfter" in data:
        import aws_sdk_healthlake.types.timestamp

        out["created_after"] = (
            aws_sdk_healthlake.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAfter"]
            )
        )
    return out
