"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseName``."""

from typing import Literal, TypeAlias, cast

LicenseName: TypeAlias = Literal["SQLServer",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseName:
    return cast(LicenseName, data)
