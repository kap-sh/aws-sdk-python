"""Generated from Smithy shape ``com.amazonaws.macie2#UsageType``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of an Amazon Macie usage metric for an account. Possible values are:</p>"""
UsageType: TypeAlias = Literal[
    "DATA_INVENTORY_EVALUATION",
    "SENSITIVE_DATA_DISCOVERY",
    "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
    "AUTOMATED_OBJECT_MONITORING",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageType) -> str:
    return value


def deserialize_json(data: str) -> UsageType:
    return cast(UsageType, data)
