"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsKeyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.kms_grant_configurations_list
    import aws_sdk_accessanalyzer.types.kms_key_policies_map


class KmsKeyConfiguration(TypedDict):
    key_policies: NotRequired[
        "aws_sdk_accessanalyzer.types.kms_key_policies_map.KmsKeyPoliciesMap"
    ]
    """<p>Resource policy configuration for the KMS key. The only valid value for the name of the key policy is <code>default</code>. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default\">Default key policy</a>.</p>"""
    grants: NotRequired[
        "aws_sdk_accessanalyzer.types.kms_grant_configurations_list.KmsGrantConfigurationsList"
    ]
    """<p>A list of proposed grant configurations for the KMS key. If the proposed grant configuration is for an existing key, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsKeyConfiguration) -> dict:
    out: dict = {}
    if "key_policies" in value:
        import aws_sdk_accessanalyzer.types.kms_key_policies_map

        out["keyPolicies"] = (
            aws_sdk_accessanalyzer.types.kms_key_policies_map.serialize_json(
                value["key_policies"]
            )
        )
    if "grants" in value:
        import aws_sdk_accessanalyzer.types.kms_grant_configurations_list

        out["grants"] = (
            aws_sdk_accessanalyzer.types.kms_grant_configurations_list.serialize_json(
                value["grants"]
            )
        )
    return out


def deserialize_json(data: dict) -> KmsKeyConfiguration:
    out: KmsKeyConfiguration = {}  # type: ignore[typeddict-item]
    if "keyPolicies" in data:
        import aws_sdk_accessanalyzer.types.kms_key_policies_map

        out["key_policies"] = (
            aws_sdk_accessanalyzer.types.kms_key_policies_map.deserialize_json(
                data["keyPolicies"]
            )
        )
    if "grants" in data:
        import aws_sdk_accessanalyzer.types.kms_grant_configurations_list

        out["grants"] = (
            aws_sdk_accessanalyzer.types.kms_grant_configurations_list.deserialize_json(
                data["grants"]
            )
        )
    return out
