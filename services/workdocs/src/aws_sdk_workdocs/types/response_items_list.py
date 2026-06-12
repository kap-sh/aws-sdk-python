"""Generated from Smithy shape ``com.amazonaws.workdocs#ResponseItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.response_item

ResponseItemsList: TypeAlias = list["aws_sdk_workdocs.types.response_item.ResponseItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseItemsList) -> list:
    import aws_sdk_workdocs.types.response_item

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.response_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseItemsList:
    import aws_sdk_workdocs.types.response_item

    out: ResponseItemsList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.response_item.deserialize_json(item))
    return out
