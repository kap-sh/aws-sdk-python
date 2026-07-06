"""Generated from Smithy shape ``com.amazonaws.xray#IndexingRuleValueUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_xray.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.probabilistic_rule_value_update


class _IndexingRuleValueUpdate_Probabilistic(TypedDict, closed=True):
    Probabilistic: "aws_sdk_xray.types.probabilistic_rule_value_update.ProbabilisticRuleValueUpdate"


IndexingRuleValueUpdate: TypeAlias = _IndexingRuleValueUpdate_Probabilistic


# --- restJson1 ser/de ---
def serialize_json(value: IndexingRuleValueUpdate) -> dict:
    if "Probabilistic" in value:
        import aws_sdk_xray.types.probabilistic_rule_value_update

        return {
            "Probabilistic": aws_sdk_xray.types.probabilistic_rule_value_update.serialize_json(
                value["Probabilistic"]
            )
        }
    else:
        raise SerializationError("IndexingRuleValueUpdate: no variant present")


def deserialize_json(data: dict) -> IndexingRuleValueUpdate:
    if "Probabilistic" in data:
        import aws_sdk_xray.types.probabilistic_rule_value_update

        return {
            "Probabilistic": aws_sdk_xray.types.probabilistic_rule_value_update.deserialize_json(
                data["Probabilistic"]
            )
        }
    else:
        raise DeserializationError("IndexingRuleValueUpdate: no recognized variant key")
