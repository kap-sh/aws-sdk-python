"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTableBucketsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.next_token
    import aws_sdk_s3tables.types.table_bucket_summary_list


class ListTableBucketsResponse(TypedDict, closed=True):
    table_buckets: (
        "aws_sdk_s3tables.types.table_bucket_summary_list.TableBucketSummaryList"
    )
    """<p>A list of table buckets.</p>"""
    continuation_token: NotRequired["aws_sdk_s3tables.types.next_token.NextToken"]
    """<p>You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableBucketsResponse) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.table_bucket_summary_list

    out["tableBuckets"] = (
        aws_sdk_s3tables.types.table_bucket_summary_list.serialize_json(
            value["table_buckets"]
        )
    )
    if "continuation_token" in value:
        out["continuationToken"] = value["continuation_token"]
    return out


def deserialize_json(data: dict) -> ListTableBucketsResponse:
    out: ListTableBucketsResponse = {}  # type: ignore[typeddict-item]
    if "tableBuckets" in data:
        import aws_sdk_s3tables.types.table_bucket_summary_list

        out["table_buckets"] = (
            aws_sdk_s3tables.types.table_bucket_summary_list.deserialize_json(
                data["tableBuckets"]
            )
        )
    else:
        raise DeserializationError("ListTableBucketsResponse.table_buckets required")
    if "continuationToken" in data:
        out["continuation_token"] = data["continuationToken"]
    return out
