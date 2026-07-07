"""Generated from Smithy shape ``com.amazonaws.xray#IndexingRuleValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_xray.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.probabilistic_rule_value


class _IndexingRuleValue_Probabilistic(TypedDict, closed=True):
    Probabilistic: "aws_sdk_xray.types.probabilistic_rule_value.ProbabilisticRuleValue"


IndexingRuleValue: TypeAlias = _IndexingRuleValue_Probabilistic


# --- restJson1 ser/de ---
def serialize_json(value: IndexingRuleValue) -> dict:
    if "Probabilistic" in value:
        import aws_sdk_xray.types.probabilistic_rule_value

        return {
            "Probabilistic": aws_sdk_xray.types.probabilistic_rule_value.serialize_json(
                value["Probabilistic"]
            )
        }
    else:
        raise SerializationError("IndexingRuleValue: no variant present")


def deserialize_json(data: dict) -> IndexingRuleValue:
    if "Probabilistic" in data:
        import aws_sdk_xray.types.probabilistic_rule_value

        return {
            "Probabilistic": aws_sdk_xray.types.probabilistic_rule_value.deserialize_json(
                data["Probabilistic"]
            )
        }
    else:
        raise DeserializationError("IndexingRuleValue: no recognized variant key")
