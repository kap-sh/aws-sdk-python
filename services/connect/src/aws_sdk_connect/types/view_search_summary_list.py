"""Generated from Smithy shape ``com.amazonaws.connect#ViewSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.view

ViewSearchSummaryList: TypeAlias = list["aws_sdk_connect.types.view.View"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewSearchSummaryList) -> list:
    import aws_sdk_connect.types.view

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.view.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewSearchSummaryList:
    import aws_sdk_connect.types.view

    out: ViewSearchSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.view.deserialize_json(item))
    return out
