"""Generated from Smithy shape ``com.amazonaws.s3tables#GetNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.table_bucket_arn


class GetNamespaceRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The name of the namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNamespaceRequest:
    out: GetNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
