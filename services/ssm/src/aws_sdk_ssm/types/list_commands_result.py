"""Generated from Smithy shape ``com.amazonaws.ssm#ListCommandsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.command_list
    import aws_sdk_ssm.types.next_token


class ListCommandsResult(TypedDict):
    commands: NotRequired["aws_sdk_ssm.types.command_list.CommandList"]
    """<p>(Optional) The list of commands requested by the user. </p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandsResult) -> dict:
    out: dict = {}
    if "commands" in value:
        import aws_sdk_ssm.types.command_list

        out["Commands"] = aws_sdk_ssm.types.command_list.serialize_aws_json_1_1(
            value["commands"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandsResult:
    out: ListCommandsResult = {}  # type: ignore[typeddict-item]
    if "Commands" in data:
        import aws_sdk_ssm.types.command_list

        out["commands"] = aws_sdk_ssm.types.command_list.deserialize_aws_json_1_1(
            data["Commands"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
