"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListStreamGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.next_token
    import aws_sdk_gameliftstreams.types.stream_group_summary_list


class ListStreamGroupsOutput(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_gameliftstreams.types.stream_group_summary_list.StreamGroupSummaryList"
    ]
    """<p>A collection of Amazon GameLift Streams stream groups that are associated with the Amazon Web Services account in use. Each item includes stream group metadata and status, but doesn't include capacity information.</p>"""
    next_token: NotRequired["aws_sdk_gameliftstreams.types.next_token.NextToken"]
    """<p>A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamGroupsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_gameliftstreams.types.stream_group_summary_list

        out["Items"] = (
            aws_sdk_gameliftstreams.types.stream_group_summary_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamGroupsOutput:
    out: ListStreamGroupsOutput = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_gameliftstreams.types.stream_group_summary_list

        out["items"] = (
            aws_sdk_gameliftstreams.types.stream_group_summary_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
