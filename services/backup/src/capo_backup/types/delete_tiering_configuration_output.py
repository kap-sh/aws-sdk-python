"""Generated from Smithy shape ``com.amazonaws.backup#DeleteTieringConfigurationOutput``."""

from typing_extensions import TypedDict


class DeleteTieringConfigurationOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTieringConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTieringConfigurationOutput:
    out: DeleteTieringConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
