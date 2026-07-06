"""Generated from Smithy shape ``com.amazonaws.sfn#ListStateMachineAliasesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.page_token
    import aws_sdk_sfn.types.state_machine_alias_list


class ListStateMachineAliasesOutput(TypedDict, closed=True):
    state_machine_aliases: (
        "aws_sdk_sfn.types.state_machine_alias_list.StateMachineAliasList"
    )
    """<p>Aliases for the state machine.</p>"""
    next_token: NotRequired["aws_sdk_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStateMachineAliasesOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.state_machine_alias_list

    out["stateMachineAliases"] = (
        aws_sdk_sfn.types.state_machine_alias_list.serialize_aws_json_1_0(
            value["state_machine_aliases"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStateMachineAliasesOutput:
    out: ListStateMachineAliasesOutput = {}  # type: ignore[typeddict-item]
    if "stateMachineAliases" in data:
        import aws_sdk_sfn.types.state_machine_alias_list

        out["state_machine_aliases"] = (
            aws_sdk_sfn.types.state_machine_alias_list.deserialize_aws_json_1_0(
                data["stateMachineAliases"]
            )
        )
    else:
        raise DeserializationError(
            "ListStateMachineAliasesOutput.state_machine_aliases required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
