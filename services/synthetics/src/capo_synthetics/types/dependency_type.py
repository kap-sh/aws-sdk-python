"""Generated from Smithy shape ``com.amazonaws.synthetics#DependencyType``."""

from typing import Literal, TypeAlias, cast

DependencyType: TypeAlias = Literal["LambdaLayer",]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyType) -> str:
    return value


def deserialize_json(data: str) -> DependencyType:
    return cast(DependencyType, data)
