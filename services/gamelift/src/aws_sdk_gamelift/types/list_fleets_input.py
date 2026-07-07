"""Generated from Smithy shape ``com.amazonaws.gamelift#ListFleetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_id_or_arn
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.positive_integer
    import aws_sdk_gamelift.types.script_id_or_arn


class ListFleetsInput(TypedDict, closed=True):
    build_id: NotRequired["aws_sdk_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>A unique identifier for the build to request fleets for. Use this parameter to return only fleets using a specified build. Use either the build ID or ARN value.</p>"""
    script_id: NotRequired["aws_sdk_gamelift.types.script_id_or_arn.ScriptIdOrArn"]
    """<p>A unique identifier for the Realtime script to request fleets for. Use this parameter to return only fleets using a specified script. Use either the script ID or ARN value.</p>"""
    limit: NotRequired["aws_sdk_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFleetsInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFleetsInput:
    out: ListFleetsInput = {}  # type: ignore[typeddict-item]
    if "BuildId" in data:
        out["build_id"] = data["BuildId"]
    if "ScriptId" in data:
        out["script_id"] = data["ScriptId"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
