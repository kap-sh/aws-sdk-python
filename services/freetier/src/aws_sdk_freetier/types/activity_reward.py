"""Generated from Smithy shape ``com.amazonaws.freetier#ActivityReward``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_freetier.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_freetier.types.monetary_amount

class _ActivityReward_credit(TypedDict):
    credit: "aws_sdk_freetier.types.monetary_amount.MonetaryAmount"

ActivityReward: TypeAlias = _ActivityReward_credit

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityReward) -> dict:
    if "credit" in value:
        import aws_sdk_freetier.types.monetary_amount
        return {"credit": aws_sdk_freetier.types.monetary_amount.serialize_aws_json_1_0(value["credit"])}
    else:
        raise SerializationError("ActivityReward: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ActivityReward:
    if "credit" in data:
        import aws_sdk_freetier.types.monetary_amount
        return {"credit": aws_sdk_freetier.types.monetary_amount.deserialize_aws_json_1_0(data["credit"])}
    else:
        raise DeserializationError("ActivityReward: no recognized variant key")