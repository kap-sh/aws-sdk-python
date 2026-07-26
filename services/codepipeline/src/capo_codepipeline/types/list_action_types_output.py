"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListActionTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_list
    import capo_codepipeline.types.next_token


class ListActionTypesOutput(TypedDict, closed=True):
    action_types: "capo_codepipeline.types.action_type_list.ActionTypeList"
    """<p>Provides details of the action types.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list action types call to return the next set of action types in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActionTypesOutput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_list

    out["actionTypes"] = (
        capo_codepipeline.types.action_type_list.serialize_aws_json_1_1(
            value["action_types"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActionTypesOutput:
    out: ListActionTypesOutput = {}  # type: ignore[typeddict-item]
    if "actionTypes" in data:
        import capo_codepipeline.types.action_type_list

        out["action_types"] = (
            capo_codepipeline.types.action_type_list.deserialize_aws_json_1_1(
                data["actionTypes"]
            )
        )
    else:
        raise DeserializationError("ListActionTypesOutput.action_types required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
