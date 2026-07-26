"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReleaseStatusValues``."""

from typing import Literal, TypeAlias, cast

ReleaseStatusValues: TypeAlias = Literal[
    "beta",
    "prod",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseStatusValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReleaseStatusValues:
    return cast(ReleaseStatusValues, data)
