"""Generated from Smithy shape ``com.amazonaws.codecatalyst#PersistentStorageConfiguration``."""

from typing import TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError


class PersistentStorageConfiguration(TypedDict):
    size_in_gi_b: "int"
    """<p>The size of the persistent storage in gigabytes (specifically GiB).</p> <note> <p>Valid values for storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersistentStorageConfiguration) -> dict:
    out: dict = {}
    out["sizeInGiB"] = value["size_in_gi_b"]
    return out


def deserialize_json(data: dict) -> PersistentStorageConfiguration:
    out: PersistentStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "sizeInGiB" in data:
        out["size_in_gi_b"] = data["sizeInGiB"]
    else:
        raise DeserializationError(
            "PersistentStorageConfiguration.size_in_gi_b required"
        )
    return out
