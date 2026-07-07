"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.analysis
    import aws_sdk_mailmanager.types.rule_boolean_email_attribute
    import aws_sdk_mailmanager.types.rule_is_in_address_list


class _RuleBooleanToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "aws_sdk_mailmanager.types.rule_boolean_email_attribute.RuleBooleanEmailAttribute"


class _RuleBooleanToEvaluate_Analysis(TypedDict, closed=True):
    Analysis: "aws_sdk_mailmanager.types.analysis.Analysis"


class _RuleBooleanToEvaluate_IsInAddressList(TypedDict, closed=True):
    IsInAddressList: (
        "aws_sdk_mailmanager.types.rule_is_in_address_list.RuleIsInAddressList"
    )


RuleBooleanToEvaluate: TypeAlias = (
    _RuleBooleanToEvaluate_Attribute
    | _RuleBooleanToEvaluate_Analysis
    | _RuleBooleanToEvaluate_IsInAddressList
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleBooleanToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.rule_boolean_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.rule_boolean_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "Analysis" in value:
        import aws_sdk_mailmanager.types.analysis

        return {
            "Analysis": aws_sdk_mailmanager.types.analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    elif "IsInAddressList" in value:
        import aws_sdk_mailmanager.types.rule_is_in_address_list

        return {
            "IsInAddressList": aws_sdk_mailmanager.types.rule_is_in_address_list.serialize_aws_json_1_0(
                value["IsInAddressList"]
            )
        }
    else:
        raise SerializationError("RuleBooleanToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleBooleanToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.rule_boolean_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.rule_boolean_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif "Analysis" in data:
        import aws_sdk_mailmanager.types.analysis

        return {
            "Analysis": aws_sdk_mailmanager.types.analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    elif "IsInAddressList" in data:
        import aws_sdk_mailmanager.types.rule_is_in_address_list

        return {
            "IsInAddressList": aws_sdk_mailmanager.types.rule_is_in_address_list.deserialize_aws_json_1_0(
                data["IsInAddressList"]
            )
        }
    else:
        raise DeserializationError("RuleBooleanToEvaluate: no recognized variant key")
