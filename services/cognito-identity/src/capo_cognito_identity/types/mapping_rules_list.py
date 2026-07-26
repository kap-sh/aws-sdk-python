"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MappingRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.mapping_rule

MappingRulesList: TypeAlias = list[
    "capo_cognito_identity.types.mapping_rule.MappingRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingRulesList) -> list:
    import capo_cognito_identity.types.mapping_rule

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity.types.mapping_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MappingRulesList:
    import capo_cognito_identity.types.mapping_rule

    out: MappingRulesList = []
    for item in data:
        out.append(
            capo_cognito_identity.types.mapping_rule.deserialize_aws_json_1_1(item)
        )
    return out
