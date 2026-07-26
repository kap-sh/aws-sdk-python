"""Generated from Smithy shape ``com.amazonaws.s3tables#ListNamespacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.list_namespaces_limit
    import capo_s3tables.types.next_token
    import capo_s3tables.types.table_bucket_arn


class ListNamespacesRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    prefix: NotRequired["str"]
    """<p>The prefix of the namespaces.</p>"""
    continuation_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""
    max_namespaces: NotRequired[
        "capo_s3tables.types.list_namespaces_limit.ListNamespacesLimit"
    ]
    """<p>The maximum number of namespaces to return in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNamespacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNamespacesRequest:
    out: ListNamespacesRequest = {}  # type: ignore[typeddict-item]
    return out
