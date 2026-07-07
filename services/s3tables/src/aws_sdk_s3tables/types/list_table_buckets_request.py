"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTableBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.list_table_buckets_limit
    import aws_sdk_s3tables.types.next_token
    import aws_sdk_s3tables.types.table_bucket_type


class ListTableBucketsRequest(TypedDict, closed=True):
    prefix: NotRequired["str"]
    """<p>The prefix of the table buckets.</p>"""
    continuation_token: NotRequired["aws_sdk_s3tables.types.next_token.NextToken"]
    """<p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""
    max_buckets: NotRequired[
        "aws_sdk_s3tables.types.list_table_buckets_limit.ListTableBucketsLimit"
    ]
    """<p>The maximum number of table buckets to return in the list.</p>"""
    type: NotRequired["aws_sdk_s3tables.types.table_bucket_type.TableBucketType"]
    """<p>The type of table buckets to filter by in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableBucketsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTableBucketsRequest:
    out: ListTableBucketsRequest = {}  # type: ignore[typeddict-item]
    return out
