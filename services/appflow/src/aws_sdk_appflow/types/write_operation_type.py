"""Generated from Smithy shape ``com.amazonaws.appflow#WriteOperationType``."""

from typing import Literal, TypeAlias, cast

"""<p> The possible write operations in the destination connector. When this value is not provided, this defaults to the <code>INSERT</code> operation. </p>"""
WriteOperationType: TypeAlias = Literal[
    "INSERT",
    "UPSERT",
    "UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: WriteOperationType) -> str:
    return value


def deserialize_json(data: str) -> WriteOperationType:
    return cast(WriteOperationType, data)
