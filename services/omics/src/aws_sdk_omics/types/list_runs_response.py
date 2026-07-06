"""Generated from Smithy shape ``com.amazonaws.omics#ListRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_list
    import aws_sdk_omics.types.run_list_token


class ListRunsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_omics.types.run_list.RunList"]
    """<p>A list of runs.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.run_list_token.RunListToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_omics.types.run_list

        out["items"] = aws_sdk_omics.types.run_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRunsResponse:
    out: ListRunsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_omics.types.run_list

        out["items"] = aws_sdk_omics.types.run_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
