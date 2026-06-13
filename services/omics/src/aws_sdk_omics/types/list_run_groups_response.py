"""Generated from Smithy shape ``com.amazonaws.omics#ListRunGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_list
    import aws_sdk_omics.types.run_group_list_token


class ListRunGroupsResponse(TypedDict):
    items: NotRequired["aws_sdk_omics.types.run_group_list.RunGroupList"]
    """<p>A list of groups.</p>"""
    next_token: NotRequired[
        "aws_sdk_omics.types.run_group_list_token.RunGroupListToken"
    ]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunGroupsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_omics.types.run_group_list

        out["items"] = aws_sdk_omics.types.run_group_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRunGroupsResponse:
    out: ListRunGroupsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_omics.types.run_group_list

        out["items"] = aws_sdk_omics.types.run_group_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
