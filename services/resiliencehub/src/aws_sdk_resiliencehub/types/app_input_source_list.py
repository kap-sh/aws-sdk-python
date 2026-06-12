"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppInputSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_input_source

AppInputSourceList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.app_input_source.AppInputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInputSourceList) -> list:
    import aws_sdk_resiliencehub.types.app_input_source

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.app_input_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppInputSourceList:
    import aws_sdk_resiliencehub.types.app_input_source

    out: AppInputSourceList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.app_input_source.deserialize_json(item))
    return out
