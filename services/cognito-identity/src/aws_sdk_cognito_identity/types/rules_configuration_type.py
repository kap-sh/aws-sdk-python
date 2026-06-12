"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RulesConfigurationType``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.mapping_rules_list


class RulesConfigurationType(TypedDict):
    rules: "aws_sdk_cognito_identity.types.mapping_rules_list.MappingRulesList"
    """<p>An array of rules. You can specify up to 25 rules per identity provider.</p> <p>Rules are evaluated in order. The first one to match specifies the role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RulesConfigurationType) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity.types.mapping_rules_list

    out["Rules"] = (
        aws_sdk_cognito_identity.types.mapping_rules_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RulesConfigurationType:
    out: RulesConfigurationType = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_cognito_identity.types.mapping_rules_list

        out["rules"] = (
            aws_sdk_cognito_identity.types.mapping_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("RulesConfigurationType.rules required")
    return out
