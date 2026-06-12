"""Generated from Smithy shape ``com.amazonaws.machinelearning#EntityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

"""<p>Object status with the following possible values:</p> <ul> <li> <p> <code>PENDING</code> </p> </li> <li> <p> <code>INPROGRESS</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>COMPLETED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
EntityStatus: TypeAlias = Literal[
    "PENDING",
    "INPROGRESS",
    "FAILED",
    "COMPLETED",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "INPROGRESS",
        "FAILED",
        "COMPLETED",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: EntityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityStatus value: {data!r}")
    return cast(EntityStatus, data)
