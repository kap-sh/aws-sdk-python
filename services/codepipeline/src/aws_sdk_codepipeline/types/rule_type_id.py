"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleTypeId``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.rule_category
    import aws_sdk_codepipeline.types.rule_owner
    import aws_sdk_codepipeline.types.rule_provider
    import aws_sdk_codepipeline.types.version


class RuleTypeId(TypedDict):
    category: "aws_sdk_codepipeline.types.rule_category.RuleCategory"
    """<p>A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is <code>Rule</code>. </p>"""
    owner: NotRequired["aws_sdk_codepipeline.types.rule_owner.RuleOwner"]
    """<p>The creator of the rule being called. The valid value for the <code>Owner</code> field in the rule category is <code>AWS</code>. </p>"""
    provider: "aws_sdk_codepipeline.types.rule_provider.RuleProvider"
    """<p>The rule provider, such as the <code>DeploymentWindow</code> rule. For a list of rule provider names, see the rules listed in the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html\">CodePipeline rule reference</a>.</p>"""
    version: NotRequired["aws_sdk_codepipeline.types.version.Version"]
    """<p>A string that describes the rule version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleTypeId) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.rule_category

    out["category"] = aws_sdk_codepipeline.types.rule_category.serialize_aws_json_1_1(
        value["category"]
    )
    if "owner" in value:
        import aws_sdk_codepipeline.types.rule_owner

        out["owner"] = aws_sdk_codepipeline.types.rule_owner.serialize_aws_json_1_1(
            value["owner"]
        )
    out["provider"] = value["provider"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleTypeId:
    out: RuleTypeId = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_codepipeline.types.rule_category

        out["category"] = (
            aws_sdk_codepipeline.types.rule_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        raise DeserializationError("RuleTypeId.category required")
    if "owner" in data:
        import aws_sdk_codepipeline.types.rule_owner

        out["owner"] = aws_sdk_codepipeline.types.rule_owner.deserialize_aws_json_1_1(
            data["owner"]
        )
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RuleTypeId.provider required")
    if "version" in data:
        out["version"] = data["version"]
    return out
