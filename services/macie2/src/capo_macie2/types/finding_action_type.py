"""Generated from Smithy shape ``com.amazonaws.macie2#FindingActionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of action that occurred for the resource and produced the policy finding:</p>"""
FindingActionType: TypeAlias = Literal["AWS_API_CALL",]


# --- restJson1 ser/de ---
def serialize_json(value: FindingActionType) -> str:
    return value


def deserialize_json(data: str) -> FindingActionType:
    return cast(FindingActionType, data)
