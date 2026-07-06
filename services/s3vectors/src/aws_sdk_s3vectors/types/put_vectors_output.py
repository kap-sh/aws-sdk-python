"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutVectorsOutput``."""

from typing_extensions import TypedDict


class PutVectorsOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutVectorsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutVectorsOutput:
    out: PutVectorsOutput = {}  # type: ignore[typeddict-item]
    return out
