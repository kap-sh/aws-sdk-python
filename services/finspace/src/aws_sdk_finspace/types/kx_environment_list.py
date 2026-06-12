"""Generated from Smithy shape ``com.amazonaws.finspace#KxEnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_environment

KxEnvironmentList: TypeAlias = list[
    "aws_sdk_finspace.types.kx_environment.KxEnvironment"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxEnvironmentList) -> list:
    import aws_sdk_finspace.types.kx_environment

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_environment.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxEnvironmentList:
    import aws_sdk_finspace.types.kx_environment

    out: KxEnvironmentList = []
    for item in data:
        out.append(aws_sdk_finspace.types.kx_environment.deserialize_json(item))
    return out
