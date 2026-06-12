"""Generated from Smithy shape ``com.amazonaws.sfn#ListMapRunsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.map_run_list
    import aws_sdk_sfn.types.page_token


class ListMapRunsOutput(TypedDict):
    map_runs: "aws_sdk_sfn.types.map_run_list.MapRunList"
    """<p>An array that lists information related to a Map Run, such as the Amazon Resource Name (ARN) of the Map Run and the ARN of the state machine that started the Map Run.</p>"""
    next_token: NotRequired["aws_sdk_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMapRunsOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.map_run_list

    out["mapRuns"] = aws_sdk_sfn.types.map_run_list.serialize_aws_json_1_0(
        value["map_runs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMapRunsOutput:
    out: ListMapRunsOutput = {}  # type: ignore[typeddict-item]
    if "mapRuns" in data:
        import aws_sdk_sfn.types.map_run_list

        out["map_runs"] = aws_sdk_sfn.types.map_run_list.deserialize_aws_json_1_0(
            data["mapRuns"]
        )
    else:
        raise DeserializationError("ListMapRunsOutput.map_runs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
