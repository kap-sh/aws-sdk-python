"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.table_bucket_arn


class CreateNamespaceResponse(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket the namespace was created in.</p>"""
    namespace: "capo_s3tables.types.namespace_list.NamespaceList"
    """<p>The name of the namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNamespaceResponse) -> dict:
    out: dict = {}
    out["tableBucketARN"] = value["table_bucket_arn"]
    import capo_s3tables.types.namespace_list

    out["namespace"] = capo_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    return out


def deserialize_json(data: dict) -> CreateNamespaceResponse:
    out: CreateNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "tableBucketARN" in data:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        raise DeserializationError("CreateNamespaceResponse.table_bucket_arn required")
    if "namespace" in data:
        import capo_s3tables.types.namespace_list

        out["namespace"] = capo_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        raise DeserializationError("CreateNamespaceResponse.namespace required")
    return out
