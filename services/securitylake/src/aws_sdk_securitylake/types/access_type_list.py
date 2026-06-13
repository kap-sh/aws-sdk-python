"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.access_type

AccessTypeList: TypeAlias = list["aws_sdk_securitylake.types.access_type.AccessType"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessTypeList) -> list:
    import aws_sdk_securitylake.types.access_type

    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.access_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessTypeList:
    import aws_sdk_securitylake.types.access_type

    out: AccessTypeList = []
    for item in data:
        out.append(aws_sdk_securitylake.types.access_type.deserialize_json(item))
    return out
