"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AbortCriteriaAction``."""

from typing import Literal, TypeAlias, cast

AbortCriteriaAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
def serialize_json(value: AbortCriteriaAction) -> str:
    return value


def deserialize_json(data: str) -> AbortCriteriaAction:
    return cast(AbortCriteriaAction, data)
