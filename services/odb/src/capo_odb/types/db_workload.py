"""Generated from Smithy shape ``com.amazonaws.odb#DbWorkload``."""

from typing import Literal, TypeAlias, cast

DbWorkload: TypeAlias = Literal[
    "OLTP",
    "AJD",
    "APEX",
    "LH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbWorkload) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbWorkload:
    return cast(DbWorkload, data)
