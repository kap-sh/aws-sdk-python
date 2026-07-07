"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_list
    import aws_sdk_s3tables.types.table_bucket_arn


class CreateNamespaceRequest(TypedDict, closed=True):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket to create the namespace in.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_list.NamespaceList"
    """<p>A name for the namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNamespaceRequest) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.namespace_list

    out["namespace"] = aws_sdk_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    return out


def deserialize_json(data: dict) -> CreateNamespaceRequest:
    out: CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_s3tables.types.namespace_list

        out["namespace"] = aws_sdk_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        raise DeserializationError("CreateNamespaceRequest.namespace required")
    return out
