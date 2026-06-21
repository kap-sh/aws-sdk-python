"""Generated from Smithy shape ``com.amazonaws.healthlake#FHIRVersion``."""

from typing import Literal, TypeAlias, cast

FHIRVersion: TypeAlias = Literal["R4",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FHIRVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FHIRVersion:
    return cast(FHIRVersion, data)
