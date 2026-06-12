"""Generated from Smithy shape ``com.amazonaws.codepipeline#UpdateActionTypeInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_type_declaration


class UpdateActionTypeInput(TypedDict):
    action_type: (
        "aws_sdk_codepipeline.types.action_type_declaration.ActionTypeDeclaration"
    )
    """<p>The action type definition for the action type to be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateActionTypeInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_type_declaration

    out["actionType"] = (
        aws_sdk_codepipeline.types.action_type_declaration.serialize_aws_json_1_1(
            value["action_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateActionTypeInput:
    out: UpdateActionTypeInput = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        import aws_sdk_codepipeline.types.action_type_declaration

        out["action_type"] = (
            aws_sdk_codepipeline.types.action_type_declaration.deserialize_aws_json_1_1(
                data["actionType"]
            )
        )
    else:
        raise DeserializationError("UpdateActionTypeInput.action_type required")
    return out
