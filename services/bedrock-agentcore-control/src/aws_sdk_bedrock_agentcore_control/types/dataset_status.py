"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

"""<p> Dataset lifecycle and operation status. </p>"""
DatasetStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetStatus:
    return cast(DatasetStatus, data)
