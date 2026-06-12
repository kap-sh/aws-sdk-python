"""Generated from Smithy shape ``com.amazonaws.connect#InitiationMethodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_initiation_method

InitiationMethodList: TypeAlias = list[
    "aws_sdk_connect.types.contact_initiation_method.ContactInitiationMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: InitiationMethodList) -> list:
    import aws_sdk_connect.types.contact_initiation_method

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_initiation_method.serialize_json(item))
    return out


def deserialize_json(data: list) -> InitiationMethodList:
    import aws_sdk_connect.types.contact_initiation_method

    out: InitiationMethodList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_initiation_method.deserialize_json(item)
        )
    return out
