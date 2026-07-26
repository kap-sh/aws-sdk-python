"""Generated from Smithy shape ``com.amazonaws.amp#IgnoreNearExpected``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError


class _IgnoreNearExpected_amount(TypedDict, closed=True):
    amount: "float"


class _IgnoreNearExpected_ratio(TypedDict, closed=True):
    ratio: "float"


IgnoreNearExpected: TypeAlias = _IgnoreNearExpected_amount | _IgnoreNearExpected_ratio


# --- restJson1 ser/de ---
def serialize_json(value: IgnoreNearExpected) -> dict:
    if "amount" in value:
        return {"amount": value["amount"]}
    elif "ratio" in value:
        return {"ratio": value["ratio"]}
    else:
        raise SerializationError("IgnoreNearExpected: no variant present")


def deserialize_json(data: dict) -> IgnoreNearExpected:
    if "amount" in data:
        return {"amount": data["amount"]}
    elif "ratio" in data:
        return {"ratio": data["ratio"]}
    else:
        raise DeserializationError("IgnoreNearExpected: no recognized variant key")
