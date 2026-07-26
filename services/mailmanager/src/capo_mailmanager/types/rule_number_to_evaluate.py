"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleNumberToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_number_email_attribute


class _RuleNumberToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: (
        "capo_mailmanager.types.rule_number_email_attribute.RuleNumberEmailAttribute"
    )


RuleNumberToEvaluate: TypeAlias = _RuleNumberToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleNumberToEvaluate) -> dict:
    if "Attribute" in value:
        import capo_mailmanager.types.rule_number_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_number_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("RuleNumberToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleNumberToEvaluate:
    if "Attribute" in data:
        import capo_mailmanager.types.rule_number_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_number_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError("RuleNumberToEvaluate: no recognized variant key")
