"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInIntentSortAttribute``."""

from typing import Literal, TypeAlias, cast

BuiltInIntentSortAttribute: TypeAlias = Literal["IntentSignature",]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInIntentSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BuiltInIntentSortAttribute:
    return cast(BuiltInIntentSortAttribute, data)
