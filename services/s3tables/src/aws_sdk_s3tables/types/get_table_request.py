"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_name


class GetTableRequest(TypedDict, closed=True):
    table_bucket_arn: NotRequired[
        "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the table bucket associated with the table.</p>"""
    namespace: NotRequired["aws_sdk_s3tables.types.namespace_name.NamespaceName"]
    """<p>The name of the namespace the table is associated with.</p>"""
    name: NotRequired["aws_sdk_s3tables.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    table_arn: NotRequired["aws_sdk_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableRequest:
    out: GetTableRequest = {}  # type: ignore[typeddict-item]
    return out
