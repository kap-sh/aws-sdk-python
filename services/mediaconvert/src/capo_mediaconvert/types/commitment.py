"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Commitment``."""

from typing import Literal, TypeAlias, cast

"""The length of the term of your reserved queue pricing plan commitment."""
Commitment: TypeAlias = Literal["ONE_YEAR",]


# --- restJson1 ser/de ---
def serialize_json(value: Commitment) -> str:
    return value


def deserialize_json(data: str) -> Commitment:
    return cast(Commitment, data)
