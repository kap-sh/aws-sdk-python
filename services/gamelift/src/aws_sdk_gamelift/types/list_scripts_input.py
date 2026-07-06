"""Generated from Smithy shape ``com.amazonaws.gamelift#ListScriptsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string
    import aws_sdk_gamelift.types.positive_integer


class ListScriptsInput(TypedDict, closed=True):
    limit: NotRequired["aws_sdk_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScriptsInput) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScriptsInput:
    out: ListScriptsInput = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
