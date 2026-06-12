"""Generated from Smithy shape ``com.amazonaws.fms#PolicyTypeScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.security_service_type_list


class PolicyTypeScope(TypedDict):
    policy_types: NotRequired[
        "aws_sdk_fms.types.security_service_type_list.SecurityServiceTypeList"
    ]
    """<p>The list of policy types that the specified Firewall Manager administrator can manage.</p>"""
    all_policy_types_enabled: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Allows the specified Firewall Manager administrator to manage all Firewall Manager policy types, except for third-party policy types. Third-party policy types can only be managed by the Firewall Manager default administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypeScope) -> dict:
    out: dict = {}
    if "policy_types" in value:
        import aws_sdk_fms.types.security_service_type_list

        out["PolicyTypes"] = (
            aws_sdk_fms.types.security_service_type_list.serialize_aws_json_1_1(
                value["policy_types"]
            )
        )
    out["AllPolicyTypesEnabled"] = value.get("all_policy_types_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyTypeScope:
    out: PolicyTypeScope = {}  # type: ignore[typeddict-item]
    if "PolicyTypes" in data:
        import aws_sdk_fms.types.security_service_type_list

        out["policy_types"] = (
            aws_sdk_fms.types.security_service_type_list.deserialize_aws_json_1_1(
                data["PolicyTypes"]
            )
        )
    if "AllPolicyTypesEnabled" in data:
        out["all_policy_types_enabled"] = data["AllPolicyTypesEnabled"]
    else:
        out["all_policy_types_enabled"] = False
    return out
