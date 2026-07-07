"""Generated from Smithy shape ``com.amazonaws.dsql#CreateClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dsql.types.bypass_policy_lockout_safety_check
    import aws_sdk_dsql.types.client_token
    import aws_sdk_dsql.types.deletion_protection_enabled
    import aws_sdk_dsql.types.kms_encryption_key
    import aws_sdk_dsql.types.multi_region_properties
    import aws_sdk_dsql.types.policy_document
    import aws_sdk_dsql.types.tag_map


class CreateClusterInput(TypedDict, closed=True):
    deletion_protection_enabled: (
        "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
    )
    """<p>If enabled, you can't delete your cluster. You must first disable this property before you can delete your cluster.</p>"""
    kms_encryption_key: NotRequired[
        "aws_sdk_dsql.types.kms_encryption_key.KmsEncryptionKey"
    ]
    """<p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>"""
    tags: NotRequired["aws_sdk_dsql.types.tag_map.TagMap"]
    """<p>A map of key and value pairs to use to tag your cluster.</p>"""
    client_token: NotRequired["aws_sdk_dsql.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>"""
    multi_region_properties: NotRequired[
        "aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"
    ]
    """<p>The configuration settings when creating a multi-Region cluster, including the witness region and linked cluster properties.</p>"""
    policy: NotRequired["aws_sdk_dsql.types.policy_document.PolicyDocument"]
    """<p>An optional resource-based policy document in JSON format that defines access permissions for the cluster.</p>"""
    bypass_policy_lockout_safety_check: "aws_sdk_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
    """<p>An optional field that controls whether to bypass the lockout prevention check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterInput) -> dict:
    out: dict = {}
    out["deletionProtectionEnabled"] = value.get("deletion_protection_enabled", True)
    if "kms_encryption_key" in value:
        out["kmsEncryptionKey"] = value["kms_encryption_key"]
    if "tags" in value:
        import aws_sdk_dsql.types.tag_map

        out["tags"] = aws_sdk_dsql.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "multi_region_properties" in value:
        import aws_sdk_dsql.types.multi_region_properties

        out["multiRegionProperties"] = (
            aws_sdk_dsql.types.multi_region_properties.serialize_json(
                value["multi_region_properties"]
            )
        )
    if "policy" in value:
        out["policy"] = value["policy"]
    out["bypassPolicyLockoutSafetyCheck"] = value.get(
        "bypass_policy_lockout_safety_check", False
    )
    return out


def deserialize_json(data: dict) -> CreateClusterInput:
    out: CreateClusterInput = {}  # type: ignore[typeddict-item]
    if "deletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = True
    if "kmsEncryptionKey" in data:
        out["kms_encryption_key"] = data["kmsEncryptionKey"]
    if "tags" in data:
        import aws_sdk_dsql.types.tag_map

        out["tags"] = aws_sdk_dsql.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "multiRegionProperties" in data:
        import aws_sdk_dsql.types.multi_region_properties

        out["multi_region_properties"] = (
            aws_sdk_dsql.types.multi_region_properties.deserialize_json(
                data["multiRegionProperties"]
            )
        )
    if "policy" in data:
        out["policy"] = data["policy"]
    if "bypassPolicyLockoutSafetyCheck" in data:
        out["bypass_policy_lockout_safety_check"] = data[
            "bypassPolicyLockoutSafetyCheck"
        ]
    else:
        out["bypass_policy_lockout_safety_check"] = False
    return out
