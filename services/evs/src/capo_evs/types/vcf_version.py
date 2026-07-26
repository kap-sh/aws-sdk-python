"""Generated from Smithy shape ``com.amazonaws.evs#VcfVersion``."""

from typing import Literal, TypeAlias, cast

VcfVersion: TypeAlias = Literal[
    "VCF-5.2.1",
    "VCF-5.2.2",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VcfVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VcfVersion:
    return cast(VcfVersion, data)
