"""Generated from Smithy shape ``com.amazonaws.dsql#UpdateClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dsql.types.client_token
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.deletion_protection_enabled
    import aws_sdk_dsql.types.kms_encryption_key
    import aws_sdk_dsql.types.multi_region_properties


class UpdateClusterInput(TypedDict, closed=True):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster you want to update.</p>"""
    deletion_protection_enabled: NotRequired[
        "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Specifies whether to enable deletion protection in your cluster.</p>"""
    kms_encryption_key: NotRequired[
        "aws_sdk_dsql.types.kms_encryption_key.KmsEncryptionKey"
    ]
    """<p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>"""
    client_token: NotRequired["aws_sdk_dsql.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>"""
    multi_region_properties: NotRequired[
        "aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"
    ]
    """<p>The new multi-Region cluster configuration settings to be applied during an update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterInput) -> dict:
    out: dict = {}
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "kms_encryption_key" in value:
        out["kmsEncryptionKey"] = value["kms_encryption_key"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "multi_region_properties" in value:
        import aws_sdk_dsql.types.multi_region_properties

        out["multiRegionProperties"] = (
            aws_sdk_dsql.types.multi_region_properties.serialize_json(
                value["multi_region_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterInput:
    out: UpdateClusterInput = {}  # type: ignore[typeddict-item]
    if "deletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    if "kmsEncryptionKey" in data:
        out["kms_encryption_key"] = data["kmsEncryptionKey"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "multiRegionProperties" in data:
        import aws_sdk_dsql.types.multi_region_properties

        out["multi_region_properties"] = (
            aws_sdk_dsql.types.multi_region_properties.deserialize_json(
                data["multiRegionProperties"]
            )
        )
    return out
