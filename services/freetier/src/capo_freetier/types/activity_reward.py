"""Generated from Smithy shape ``com.amazonaws.freetier#ActivityReward``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_freetier.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_freetier.types.monetary_amount


class _ActivityReward_credit(TypedDict, closed=True):
    credit: "capo_freetier.types.monetary_amount.MonetaryAmount"


ActivityReward: TypeAlias = _ActivityReward_credit


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityReward) -> dict:
    if "credit" in value:
        import capo_freetier.types.monetary_amount

        return {
            "credit": capo_freetier.types.monetary_amount.serialize_aws_json_1_0(
                value["credit"]
            )
        }
    else:
        raise SerializationError("ActivityReward: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ActivityReward:
    if "credit" in data:
        import capo_freetier.types.monetary_amount

        return {
            "credit": capo_freetier.types.monetary_amount.deserialize_aws_json_1_0(
                data["credit"]
            )
        }
    else:
        raise DeserializationError("ActivityReward: no recognized variant key")
