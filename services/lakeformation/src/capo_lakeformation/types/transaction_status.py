"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionStatus``."""

from typing import Literal, TypeAlias, cast

TransactionStatus: TypeAlias = Literal[
    "ACTIVE",
    "COMMITTED",
    "ABORTED",
    "COMMIT_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionStatus) -> str:
    return value


def deserialize_json(data: str) -> TransactionStatus:
    return cast(TransactionStatus, data)
