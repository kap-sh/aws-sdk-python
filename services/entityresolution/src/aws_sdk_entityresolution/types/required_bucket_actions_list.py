"""Generated from Smithy shape ``com.amazonaws.entityresolution#RequiredBucketActionsList``."""

from typing import TypeAlias

RequiredBucketActionsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredBucketActionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RequiredBucketActionsList:
    return list(data)
