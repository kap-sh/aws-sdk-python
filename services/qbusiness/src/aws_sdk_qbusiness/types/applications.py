"""Generated from Smithy shape ``com.amazonaws.qbusiness#Applications``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application

Applications: TypeAlias = list["aws_sdk_qbusiness.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: Applications) -> list:
    import aws_sdk_qbusiness.types.application
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> Applications:
    import aws_sdk_qbusiness.types.application
    out: Applications = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.application.deserialize_json(item))
    return out