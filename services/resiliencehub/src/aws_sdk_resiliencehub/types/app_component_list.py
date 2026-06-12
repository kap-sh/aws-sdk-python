"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_component

AppComponentList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.app_component.AppComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppComponentList) -> list:
    import aws_sdk_resiliencehub.types.app_component

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.app_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppComponentList:
    import aws_sdk_resiliencehub.types.app_component

    out: AppComponentList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.app_component.deserialize_json(item))
    return out
