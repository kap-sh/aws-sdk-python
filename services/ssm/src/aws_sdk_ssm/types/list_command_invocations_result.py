"""Generated from Smithy shape ``com.amazonaws.ssm#ListCommandInvocationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.command_invocation_list
    import aws_sdk_ssm.types.next_token


class ListCommandInvocationsResult(TypedDict, closed=True):
    command_invocations: NotRequired[
        "aws_sdk_ssm.types.command_invocation_list.CommandInvocationList"
    ]
    """<p>(Optional) A list of all invocations. </p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandInvocationsResult) -> dict:
    out: dict = {}
    if "command_invocations" in value:
        import aws_sdk_ssm.types.command_invocation_list

        out["CommandInvocations"] = (
            aws_sdk_ssm.types.command_invocation_list.serialize_aws_json_1_1(
                value["command_invocations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandInvocationsResult:
    out: ListCommandInvocationsResult = {}  # type: ignore[typeddict-item]
    if "CommandInvocations" in data:
        import aws_sdk_ssm.types.command_invocation_list

        out["command_invocations"] = (
            aws_sdk_ssm.types.command_invocation_list.deserialize_aws_json_1_1(
                data["CommandInvocations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
