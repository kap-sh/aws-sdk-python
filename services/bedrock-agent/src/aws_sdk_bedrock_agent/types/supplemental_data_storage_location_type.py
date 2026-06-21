"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupplementalDataStorageLocationType``."""

from typing import Literal, TypeAlias, cast

SupplementalDataStorageLocationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalDataStorageLocationType) -> str:
    return value


def deserialize_json(data: str) -> SupplementalDataStorageLocationType:
    return cast(SupplementalDataStorageLocationType, data)
