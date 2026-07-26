"""Generated from Smithy shape ``com.amazonaws.machinelearning#EntityStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Object status with the following possible values:</p> <ul> <li> <p> <code>PENDING</code> </p> </li> <li> <p> <code>INPROGRESS</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>COMPLETED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
EntityStatus: TypeAlias = Literal[
    "PENDING",
    "INPROGRESS",
    "FAILED",
    "COMPLETED",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityStatus:
    return cast(EntityStatus, data)
