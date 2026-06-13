"""Generated from Smithy shape ``com.amazonaws.groundstation#StatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.contact_status

StatusList: TypeAlias = list["aws_sdk_groundstation.types.contact_status.ContactStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: StatusList) -> list:
    import aws_sdk_groundstation.types.contact_status

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.contact_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatusList:
    import aws_sdk_groundstation.types.contact_status

    out: StatusList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.contact_status.deserialize_json(item))
    return out
