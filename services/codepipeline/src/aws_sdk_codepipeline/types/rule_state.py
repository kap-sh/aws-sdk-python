"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.rule_execution
    import aws_sdk_codepipeline.types.rule_name
    import aws_sdk_codepipeline.types.rule_revision
    import aws_sdk_codepipeline.types.url


class RuleState(TypedDict, closed=True):
    rule_name: NotRequired["aws_sdk_codepipeline.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    current_revision: NotRequired[
        "aws_sdk_codepipeline.types.rule_revision.RuleRevision"
    ]
    """<p>The ID of the current revision of the artifact successfully worked on by the job.</p>"""
    latest_execution: NotRequired[
        "aws_sdk_codepipeline.types.rule_execution.RuleExecution"
    ]
    """<p>Represents information about the latest run of an rule.</p>"""
    entity_url: NotRequired["aws_sdk_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the state of the action, such as a details page.</p>"""
    revision_url: NotRequired["aws_sdk_codepipeline.types.url.Url"]
    """<p>A URL link for more information about the revision, such as a commit details page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleState) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "current_revision" in value:
        import aws_sdk_codepipeline.types.rule_revision

        out["currentRevision"] = (
            aws_sdk_codepipeline.types.rule_revision.serialize_aws_json_1_1(
                value["current_revision"]
            )
        )
    if "latest_execution" in value:
        import aws_sdk_codepipeline.types.rule_execution

        out["latestExecution"] = (
            aws_sdk_codepipeline.types.rule_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleState:
    out: RuleState = {}  # type: ignore[typeddict-item]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    if "currentRevision" in data:
        import aws_sdk_codepipeline.types.rule_revision

        out["current_revision"] = (
            aws_sdk_codepipeline.types.rule_revision.deserialize_aws_json_1_1(
                data["currentRevision"]
            )
        )
    if "latestExecution" in data:
        import aws_sdk_codepipeline.types.rule_execution

        out["latest_execution"] = (
            aws_sdk_codepipeline.types.rule_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if "entityUrl" in data:
        out["entity_url"] = data["entityUrl"]
    if "revisionUrl" in data:
        out["revision_url"] = data["revisionUrl"]
    return out
