"""Generated from Smithy shape ``com.amazonaws.datazone#NetworkAccessType``."""

from typing import Literal, TypeAlias, cast

"""<p>The network access type for a notebook run in Amazon SageMaker Unified Studio.</p>"""
NetworkAccessType: TypeAlias = Literal[
    "PUBLIC_INTERNET_ONLY",
    "VPC_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAccessType) -> str:
    return value


def deserialize_json(data: str) -> NetworkAccessType:
    return cast(NetworkAccessType, data)
