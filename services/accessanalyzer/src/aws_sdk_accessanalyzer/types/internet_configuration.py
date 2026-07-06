"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternetConfiguration``."""

from typing_extensions import TypedDict


class InternetConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: InternetConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InternetConfiguration:
    out: InternetConfiguration = {}  # type: ignore[typeddict-item]
    return out
