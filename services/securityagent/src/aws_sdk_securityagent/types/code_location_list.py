"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeLocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_location

CodeLocationList: TypeAlias = list[
    "aws_sdk_securityagent.types.code_location.CodeLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeLocationList) -> list:
    import aws_sdk_securityagent.types.code_location

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.code_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeLocationList:
    import aws_sdk_securityagent.types.code_location

    out: CodeLocationList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.code_location.deserialize_json(item))
    return out
