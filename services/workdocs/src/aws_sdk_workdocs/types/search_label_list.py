"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.search_label

SearchLabelList: TypeAlias = list["aws_sdk_workdocs.types.search_label.SearchLabel"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchLabelList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchLabelList:
    return list(data)
