"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableEncryptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_name


class GetTableEncryptionRequest(TypedDict, closed=True):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket containing the table.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace associated with the table.</p>"""
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableEncryptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableEncryptionRequest:
    out: GetTableEncryptionRequest = {}  # type: ignore[typeddict-item]
    return out
