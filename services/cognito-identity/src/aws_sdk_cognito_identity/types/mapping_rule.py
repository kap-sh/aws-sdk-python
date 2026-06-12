"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MappingRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.arn_string
    import aws_sdk_cognito_identity.types.claim_name
    import aws_sdk_cognito_identity.types.claim_value
    import aws_sdk_cognito_identity.types.mapping_rule_match_type


class MappingRule(TypedDict):
    claim: "aws_sdk_cognito_identity.types.claim_name.ClaimName"
    """<p>The claim name that must be present in the token, for example, \"isAdmin\" or \"paid\".</p>"""
    match_type: (
        "aws_sdk_cognito_identity.types.mapping_rule_match_type.MappingRuleMatchType"
    )
    """<p>The match condition that specifies how closely the claim value in the IdP token must match <code>Value</code>.</p>"""
    value: "aws_sdk_cognito_identity.types.claim_value.ClaimValue"
    """<p>A brief string that the claim must match, for example, \"paid\" or \"yes\".</p>"""
    role_arn: "aws_sdk_cognito_identity.types.arn_string.ARNString"
    """<p>The role ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingRule) -> dict:
    out: dict = {}
    out["Claim"] = value["claim"]
    import aws_sdk_cognito_identity.types.mapping_rule_match_type

    out["MatchType"] = (
        aws_sdk_cognito_identity.types.mapping_rule_match_type.serialize_aws_json_1_1(
            value["match_type"]
        )
    )
    out["Value"] = value["value"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MappingRule:
    out: MappingRule = {}  # type: ignore[typeddict-item]
    if "Claim" in data:
        out["claim"] = data["Claim"]
    else:
        raise DeserializationError("MappingRule.claim required")
    if "MatchType" in data:
        import aws_sdk_cognito_identity.types.mapping_rule_match_type

        out["match_type"] = (
            aws_sdk_cognito_identity.types.mapping_rule_match_type.deserialize_aws_json_1_1(
                data["MatchType"]
            )
        )
    else:
        raise DeserializationError("MappingRule.match_type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("MappingRule.value required")
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("MappingRule.role_arn required")
    return out
