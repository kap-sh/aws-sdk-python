"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTablesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token


class ListDataTablesRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance whose data tables should be listed.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of data tables to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTablesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataTablesRequest:
    out: ListDataTablesRequest = {}  # type: ignore[typeddict-item]
    return out
