"""Generated from Smithy shape ``com.amazonaws.sfn#ListExecutionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.execution_list
    import aws_sdk_sfn.types.list_executions_page_token


class ListExecutionsOutput(TypedDict):
    executions: "aws_sdk_sfn.types.execution_list.ExecutionList"
    """<p>The list of matching executions.</p>"""
    next_token: NotRequired[
        "aws_sdk_sfn.types.list_executions_page_token.ListExecutionsPageToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExecutionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.execution_list

    out["executions"] = aws_sdk_sfn.types.execution_list.serialize_aws_json_1_0(
        value["executions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExecutionsOutput:
    out: ListExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "executions" in data:
        import aws_sdk_sfn.types.execution_list

        out["executions"] = aws_sdk_sfn.types.execution_list.deserialize_aws_json_1_0(
            data["executions"]
        )
    else:
        raise DeserializationError("ListExecutionsOutput.executions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
