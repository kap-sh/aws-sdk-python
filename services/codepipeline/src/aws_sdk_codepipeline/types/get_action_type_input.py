"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetActionTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_category
    import aws_sdk_codepipeline.types.action_provider
    import aws_sdk_codepipeline.types.action_type_owner
    import aws_sdk_codepipeline.types.version


class GetActionTypeInput(TypedDict, closed=True):
    category: "aws_sdk_codepipeline.types.action_category.ActionCategory"
    """<p>Defines what kind of action can be taken in the stage. The following are the valid values:</p> <ul> <li> <p> <code>Source</code> </p> </li> <li> <p> <code>Build</code> </p> </li> <li> <p> <code>Test</code> </p> </li> <li> <p> <code>Deploy</code> </p> </li> <li> <p> <code>Approval</code> </p> </li> <li> <p> <code>Invoke</code> </p> </li> <li> <p> <code>Compute</code> </p> </li> </ul>"""
    owner: "aws_sdk_codepipeline.types.action_type_owner.ActionTypeOwner"
    """<p>The creator of an action type that was created with any supported integration model. There are two valid values: <code>AWS</code> and <code>ThirdParty</code>.</p>"""
    provider: "aws_sdk_codepipeline.types.action_provider.ActionProvider"
    """<p>The provider of the action type being called. The provider name is specified when the action type is created.</p>"""
    version: "aws_sdk_codepipeline.types.version.Version"
    """<p>A string that describes the action type version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetActionTypeInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_category

    out["category"] = aws_sdk_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    out["owner"] = value["owner"]
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetActionTypeInput:
    out: GetActionTypeInput = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_codepipeline.types.action_category

        out["category"] = (
            aws_sdk_codepipeline.types.action_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        raise DeserializationError("GetActionTypeInput.category required")
    if "owner" in data:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("GetActionTypeInput.owner required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("GetActionTypeInput.provider required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("GetActionTypeInput.version required")
    return out
