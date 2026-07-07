"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTablePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.resource_policy
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_name


class PutTablePolicyRequest(TypedDict, closed=True):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace associated with the table.</p>"""
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    resource_policy: "aws_sdk_s3tables.types.resource_policy.ResourcePolicy"
    """<p>The <code>JSON</code> that defines the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTablePolicyRequest) -> dict:
    out: dict = {}
    out["resourcePolicy"] = value["resource_policy"]
    return out


def deserialize_json(data: dict) -> PutTablePolicyRequest:
    out: PutTablePolicyRequest = {}  # type: ignore[typeddict-item]
    if "resourcePolicy" in data:
        out["resource_policy"] = data["resourcePolicy"]
    else:
        raise DeserializationError("PutTablePolicyRequest.resource_policy required")
    return out
