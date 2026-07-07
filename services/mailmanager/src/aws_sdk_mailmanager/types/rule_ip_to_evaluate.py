"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_ip_email_attribute


class _RuleIpToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "aws_sdk_mailmanager.types.rule_ip_email_attribute.RuleIpEmailAttribute"


RuleIpToEvaluate: TypeAlias = _RuleIpToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIpToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.rule_ip_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.rule_ip_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("RuleIpToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleIpToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.rule_ip_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.rule_ip_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError("RuleIpToEvaluate: no recognized variant key")
