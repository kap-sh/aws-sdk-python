"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListDataCellsFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.page_size
    import aws_sdk_lakeformation.types.table_resource
    import aws_sdk_lakeformation.types.token


class ListDataCellsFilterRequest(TypedDict, closed=True):
    table: NotRequired["aws_sdk_lakeformation.types.table_resource.TableResource"]
    """<p>A table in the Glue Data Catalog.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    max_results: NotRequired["aws_sdk_lakeformation.types.page_size.PageSize"]
    """<p>The maximum size of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataCellsFilterRequest) -> dict:
    out: dict = {}
    if "table" in value:
        import aws_sdk_lakeformation.types.table_resource

        out["Table"] = aws_sdk_lakeformation.types.table_resource.serialize_json(
            value["table"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListDataCellsFilterRequest:
    out: ListDataCellsFilterRequest = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import aws_sdk_lakeformation.types.table_resource

        out["table"] = aws_sdk_lakeformation.types.table_resource.deserialize_json(
            data["Table"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
