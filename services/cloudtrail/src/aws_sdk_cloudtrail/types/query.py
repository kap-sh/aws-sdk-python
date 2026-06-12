"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Query``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.query_status
    import aws_sdk_cloudtrail.types.uuid


class Query(TypedDict):
    query_id: NotRequired["aws_sdk_cloudtrail.types.uuid.UUID"]
    """<p>The ID of a query.</p>"""
    query_status: NotRequired["aws_sdk_cloudtrail.types.query_status.QueryStatus"]
    """<p>The status of the query. This can be <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code>.</p>"""
    creation_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>The creation time of a query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Query) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_status" in value:
        import aws_sdk_cloudtrail.types.query_status

        out["QueryStatus"] = (
            aws_sdk_cloudtrail.types.query_status.serialize_aws_json_1_1(
                value["query_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["CreationTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Query:
    out: Query = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "QueryStatus" in data:
        import aws_sdk_cloudtrail.types.query_status

        out["query_status"] = (
            aws_sdk_cloudtrail.types.query_status.deserialize_aws_json_1_1(
                data["QueryStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["creation_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
