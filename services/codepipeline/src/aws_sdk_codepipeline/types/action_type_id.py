"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeId``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_category
    import aws_sdk_codepipeline.types.action_owner
    import aws_sdk_codepipeline.types.action_provider
    import aws_sdk_codepipeline.types.version


class ActionTypeId(TypedDict):
    category: "aws_sdk_codepipeline.types.action_category.ActionCategory"
    """<p>A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values. </p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Invoke</p> </li> <li> <p>Approval</p> </li> <li> <p>Compute</p> </li> </ul>"""
    owner: "aws_sdk_codepipeline.types.action_owner.ActionOwner"
    r"""<p>The creator of the action being called. There are three valid values for the <code>Owner</code> field in the action category section within your pipeline structure: <code>AWS</code>, <code>ThirdParty</code>, and <code>Custom</code>. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers\">Valid Action Types and Providers in CodePipeline</a>.</p>"""
    provider: "aws_sdk_codepipeline.types.action_provider.ActionProvider"
    r"""<p>The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as <code>CodeDeploy</code>. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers\">Valid Action Types and Providers in CodePipeline</a>.</p>"""
    version: "aws_sdk_codepipeline.types.version.Version"
    """<p>A string that describes the action version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeId) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_category

    out["category"] = aws_sdk_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    import aws_sdk_codepipeline.types.action_owner

    out["owner"] = aws_sdk_codepipeline.types.action_owner.serialize_aws_json_1_1(
        value["owner"]
    )
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeId:
    out: ActionTypeId = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_codepipeline.types.action_category

        out["category"] = (
            aws_sdk_codepipeline.types.action_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        raise DeserializationError("ActionTypeId.category required")
    if "owner" in data:
        import aws_sdk_codepipeline.types.action_owner

        out["owner"] = aws_sdk_codepipeline.types.action_owner.deserialize_aws_json_1_1(
            data["owner"]
        )
    else:
        raise DeserializationError("ActionTypeId.owner required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("ActionTypeId.provider required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ActionTypeId.version required")
    return out
