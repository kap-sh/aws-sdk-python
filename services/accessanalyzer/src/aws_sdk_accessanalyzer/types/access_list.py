"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access

AccessList: TypeAlias = list["aws_sdk_accessanalyzer.types.access.Access"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessList) -> list:
    import aws_sdk_accessanalyzer.types.access

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.access.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessList:
    import aws_sdk_accessanalyzer.types.access

    out: AccessList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.access.deserialize_json(item))
    return out
