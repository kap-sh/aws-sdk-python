"""Generated from Smithy shape ``com.amazonaws.s3tables#DeleteTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.version_token


class DeleteTableRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace associated with the table.</p>"""
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    version_token: NotRequired["aws_sdk_s3tables.types.version_token.VersionToken"]
    """<p>The version token of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTableRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTableRequest:
    out: DeleteTableRequest = {}  # type: ignore[typeddict-item]
    return out
