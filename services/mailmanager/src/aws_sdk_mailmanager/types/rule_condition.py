"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_boolean_expression
    import aws_sdk_mailmanager.types.rule_dmarc_expression
    import aws_sdk_mailmanager.types.rule_ip_expression
    import aws_sdk_mailmanager.types.rule_number_expression
    import aws_sdk_mailmanager.types.rule_string_expression
    import aws_sdk_mailmanager.types.rule_verdict_expression


class _RuleCondition_BooleanExpression(TypedDict, closed=True):
    BooleanExpression: (
        "aws_sdk_mailmanager.types.rule_boolean_expression.RuleBooleanExpression"
    )


class _RuleCondition_StringExpression(TypedDict, closed=True):
    StringExpression: (
        "aws_sdk_mailmanager.types.rule_string_expression.RuleStringExpression"
    )


class _RuleCondition_NumberExpression(TypedDict, closed=True):
    NumberExpression: (
        "aws_sdk_mailmanager.types.rule_number_expression.RuleNumberExpression"
    )


class _RuleCondition_IpExpression(TypedDict, closed=True):
    IpExpression: "aws_sdk_mailmanager.types.rule_ip_expression.RuleIpExpression"


class _RuleCondition_VerdictExpression(TypedDict, closed=True):
    VerdictExpression: (
        "aws_sdk_mailmanager.types.rule_verdict_expression.RuleVerdictExpression"
    )


class _RuleCondition_DmarcExpression(TypedDict, closed=True):
    DmarcExpression: (
        "aws_sdk_mailmanager.types.rule_dmarc_expression.RuleDmarcExpression"
    )


RuleCondition: TypeAlias = (
    _RuleCondition_BooleanExpression
    | _RuleCondition_StringExpression
    | _RuleCondition_NumberExpression
    | _RuleCondition_IpExpression
    | _RuleCondition_VerdictExpression
    | _RuleCondition_DmarcExpression
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleCondition) -> dict:
    if "BooleanExpression" in value:
        import aws_sdk_mailmanager.types.rule_boolean_expression

        return {
            "BooleanExpression": aws_sdk_mailmanager.types.rule_boolean_expression.serialize_aws_json_1_0(
                value["BooleanExpression"]
            )
        }
    elif "StringExpression" in value:
        import aws_sdk_mailmanager.types.rule_string_expression

        return {
            "StringExpression": aws_sdk_mailmanager.types.rule_string_expression.serialize_aws_json_1_0(
                value["StringExpression"]
            )
        }
    elif "NumberExpression" in value:
        import aws_sdk_mailmanager.types.rule_number_expression

        return {
            "NumberExpression": aws_sdk_mailmanager.types.rule_number_expression.serialize_aws_json_1_0(
                value["NumberExpression"]
            )
        }
    elif "IpExpression" in value:
        import aws_sdk_mailmanager.types.rule_ip_expression

        return {
            "IpExpression": aws_sdk_mailmanager.types.rule_ip_expression.serialize_aws_json_1_0(
                value["IpExpression"]
            )
        }
    elif "VerdictExpression" in value:
        import aws_sdk_mailmanager.types.rule_verdict_expression

        return {
            "VerdictExpression": aws_sdk_mailmanager.types.rule_verdict_expression.serialize_aws_json_1_0(
                value["VerdictExpression"]
            )
        }
    elif "DmarcExpression" in value:
        import aws_sdk_mailmanager.types.rule_dmarc_expression

        return {
            "DmarcExpression": aws_sdk_mailmanager.types.rule_dmarc_expression.serialize_aws_json_1_0(
                value["DmarcExpression"]
            )
        }
    else:
        raise SerializationError("RuleCondition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleCondition:
    if "BooleanExpression" in data:
        import aws_sdk_mailmanager.types.rule_boolean_expression

        return {
            "BooleanExpression": aws_sdk_mailmanager.types.rule_boolean_expression.deserialize_aws_json_1_0(
                data["BooleanExpression"]
            )
        }
    elif "StringExpression" in data:
        import aws_sdk_mailmanager.types.rule_string_expression

        return {
            "StringExpression": aws_sdk_mailmanager.types.rule_string_expression.deserialize_aws_json_1_0(
                data["StringExpression"]
            )
        }
    elif "NumberExpression" in data:
        import aws_sdk_mailmanager.types.rule_number_expression

        return {
            "NumberExpression": aws_sdk_mailmanager.types.rule_number_expression.deserialize_aws_json_1_0(
                data["NumberExpression"]
            )
        }
    elif "IpExpression" in data:
        import aws_sdk_mailmanager.types.rule_ip_expression

        return {
            "IpExpression": aws_sdk_mailmanager.types.rule_ip_expression.deserialize_aws_json_1_0(
                data["IpExpression"]
            )
        }
    elif "VerdictExpression" in data:
        import aws_sdk_mailmanager.types.rule_verdict_expression

        return {
            "VerdictExpression": aws_sdk_mailmanager.types.rule_verdict_expression.deserialize_aws_json_1_0(
                data["VerdictExpression"]
            )
        }
    elif "DmarcExpression" in data:
        import aws_sdk_mailmanager.types.rule_dmarc_expression

        return {
            "DmarcExpression": aws_sdk_mailmanager.types.rule_dmarc_expression.deserialize_aws_json_1_0(
                data["DmarcExpression"]
            )
        }
    else:
        raise DeserializationError("RuleCondition: no recognized variant key")
