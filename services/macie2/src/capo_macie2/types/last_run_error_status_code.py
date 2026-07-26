"""Generated from Smithy shape ``com.amazonaws.macie2#LastRunErrorStatusCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether any account- or bucket-level access errors occurred during the run of a one-time classification job or the most recent run of a recurring classification job. Possible values are:</p>"""
LastRunErrorStatusCode: TypeAlias = Literal[
    "NONE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: LastRunErrorStatusCode) -> str:
    return value


def deserialize_json(data: str) -> LastRunErrorStatusCode:
    return cast(LastRunErrorStatusCode, data)
