"""Generated from Smithy shape ``com.amazonaws.codepipeline#CreateCustomActionTypeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_type
    import aws_sdk_codepipeline.types.tag_list


class CreateCustomActionTypeOutput(TypedDict):
    action_type: "aws_sdk_codepipeline.types.action_type.ActionType"
    """<p>Returns information about the details of an action type.</p>"""
    tags: NotRequired["aws_sdk_codepipeline.types.tag_list.TagList"]
    """<p>Specifies the tags applied to the custom action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomActionTypeOutput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_type

    out["actionType"] = aws_sdk_codepipeline.types.action_type.serialize_aws_json_1_1(
        value["action_type"]
    )
    if "tags" in value:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomActionTypeOutput:
    out: CreateCustomActionTypeOutput = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        import aws_sdk_codepipeline.types.action_type

        out["action_type"] = (
            aws_sdk_codepipeline.types.action_type.deserialize_aws_json_1_1(
                data["actionType"]
            )
        )
    else:
        raise DeserializationError("CreateCustomActionTypeOutput.action_type required")
    if "tags" in data:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
