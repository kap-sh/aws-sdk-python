"""Generated from Smithy shape ``com.amazonaws.qbusiness#Principals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.principal

Principals: TypeAlias = list["aws_sdk_qbusiness.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: Principals) -> list:
    import aws_sdk_qbusiness.types.principal

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> Principals:
    import aws_sdk_qbusiness.types.principal

    out: Principals = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.principal.deserialize_json(item))
    return out
