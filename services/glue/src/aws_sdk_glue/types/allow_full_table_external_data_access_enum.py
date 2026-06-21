"""Generated from Smithy shape ``com.amazonaws.glue#AllowFullTableExternalDataAccessEnum``."""

from typing import Literal, TypeAlias, cast

AllowFullTableExternalDataAccessEnum: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowFullTableExternalDataAccessEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AllowFullTableExternalDataAccessEnum:
    return cast(AllowFullTableExternalDataAccessEnum, data)
