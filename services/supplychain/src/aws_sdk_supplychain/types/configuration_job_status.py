"""Generated from Smithy shape ``com.amazonaws.supplychain#ConfigurationJobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the job.</p>"""
ConfigurationJobStatus: TypeAlias = Literal[
    "NEW",
    "FAILED",
    "IN_PROGRESS",
    "QUEUED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationJobStatus:
    return cast(ConfigurationJobStatus, data)
