"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileStatus``."""

from typing import Literal, TypeAlias, cast

InferenceProfileStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> InferenceProfileStatus:
    return cast(InferenceProfileStatus, data)
