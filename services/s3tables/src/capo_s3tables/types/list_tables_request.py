"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.list_tables_limit
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.next_token
    import capo_s3tables.types.table_bucket_arn


class ListTablesRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon resource Name (ARN) of the table bucket.</p>"""
    namespace: NotRequired["capo_s3tables.types.namespace_name.NamespaceName"]
    """<p>The namespace of the tables.</p>"""
    prefix: NotRequired["str"]
    """<p>The prefix of the tables.</p>"""
    continuation_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""
    max_tables: NotRequired["capo_s3tables.types.list_tables_limit.ListTablesLimit"]
    """<p>The maximum number of tables to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTablesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTablesRequest:
    out: ListTablesRequest = {}  # type: ignore[typeddict-item]
    return out
