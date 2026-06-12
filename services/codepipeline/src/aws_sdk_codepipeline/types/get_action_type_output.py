"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetActionTypeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_type_declaration


class GetActionTypeOutput(TypedDict):
    action_type: NotRequired[
        "aws_sdk_codepipeline.types.action_type_declaration.ActionTypeDeclaration"
    ]
    """<p>The action type information for the requested action type, such as the action type ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetActionTypeOutput) -> dict:
    out: dict = {}
    if "action_type" in value:
        import aws_sdk_codepipeline.types.action_type_declaration

        out["actionType"] = (
            aws_sdk_codepipeline.types.action_type_declaration.serialize_aws_json_1_1(
                value["action_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetActionTypeOutput:
    out: GetActionTypeOutput = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        import aws_sdk_codepipeline.types.action_type_declaration

        out["action_type"] = (
            aws_sdk_codepipeline.types.action_type_declaration.deserialize_aws_json_1_1(
                data["actionType"]
            )
        )
    return out
