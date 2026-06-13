"""Generated from Smithy shape ``com.amazonaws.quicksight#PaginationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long
    import aws_sdk_quicksight.types.page_number


class PaginationConfiguration(TypedDict):
    page_size: "aws_sdk_quicksight.types.long.Long"
    """<p>Indicates how many items render in one page.</p>"""
    page_number: "aws_sdk_quicksight.types.page_number.PageNumber"
    """<p>Indicates the page number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaginationConfiguration) -> dict:
    out: dict = {}
    out["PageSize"] = value["page_size"]
    out["PageNumber"] = value["page_number"]
    return out


def deserialize_json(data: dict) -> PaginationConfiguration:
    out: PaginationConfiguration = {}  # type: ignore[typeddict-item]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        raise DeserializationError("PaginationConfiguration.page_size required")
    if "PageNumber" in data:
        out["page_number"] = data["PageNumber"]
    else:
        raise DeserializationError("PaginationConfiguration.page_number required")
    return out
