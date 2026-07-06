"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeleteCustomActionTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_category
    import aws_sdk_codepipeline.types.action_provider
    import aws_sdk_codepipeline.types.version


class DeleteCustomActionTypeInput(TypedDict, closed=True):
    category: "aws_sdk_codepipeline.types.action_category.ActionCategory"
    """<p>The category of the custom action that you want to delete, such as source or deploy.</p>"""
    provider: "aws_sdk_codepipeline.types.action_provider.ActionProvider"
    """<p>The provider of the service used in the custom action, such as CodeDeploy.</p>"""
    version: "aws_sdk_codepipeline.types.version.Version"
    """<p>The version of the custom action to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomActionTypeInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_category

    out["category"] = aws_sdk_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomActionTypeInput:
    out: DeleteCustomActionTypeInput = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_codepipeline.types.action_category

        out["category"] = (
            aws_sdk_codepipeline.types.action_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        raise DeserializationError("DeleteCustomActionTypeInput.category required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("DeleteCustomActionTypeInput.provider required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("DeleteCustomActionTypeInput.version required")
    return out
