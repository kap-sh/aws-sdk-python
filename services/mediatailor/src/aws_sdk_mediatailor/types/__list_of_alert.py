"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAlert``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.alert

__listOfAlert: TypeAlias = list["aws_sdk_mediatailor.types.alert.Alert"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAlert) -> list:
    import aws_sdk_mediatailor.types.alert

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.alert.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAlert:
    import aws_sdk_mediatailor.types.alert

    out: __listOfAlert = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.alert.deserialize_json(item))
    return out
