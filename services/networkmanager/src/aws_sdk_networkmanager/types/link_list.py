"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link

LinkList: TypeAlias = list["aws_sdk_networkmanager.types.link.Link"]


# --- restJson1 ser/de ---
def serialize_json(value: LinkList) -> list:
    import aws_sdk_networkmanager.types.link

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.link.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkList:
    import aws_sdk_networkmanager.types.link

    out: LinkList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.link.deserialize_json(item))
    return out
