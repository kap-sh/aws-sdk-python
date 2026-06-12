"""Generated from Smithy shape ``com.amazonaws.codebuild#ScopeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.webhook_scope_type


class ScopeConfiguration(TypedDict):
    name: "aws_sdk_codebuild.types.string.String"
    """<p>The name of either the group, enterprise, or organization that will send webhook events to CodeBuild, depending on the type of webhook.</p>"""
    domain: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The domain of the GitHub Enterprise organization or the GitLab Self Managed group. Note that this parameter is only required if your project's source type is GITHUB_ENTERPRISE or GITLAB_SELF_MANAGED.</p>"""
    scope: "aws_sdk_codebuild.types.webhook_scope_type.WebhookScopeType"
    """<p>The type of scope for a GitHub or GitLab webhook. The scope default is GITHUB_ORGANIZATION.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "domain" in value:
        out["domain"] = value["domain"]
    import aws_sdk_codebuild.types.webhook_scope_type

    out["scope"] = aws_sdk_codebuild.types.webhook_scope_type.serialize_aws_json_1_1(
        value["scope"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScopeConfiguration:
    out: ScopeConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ScopeConfiguration.name required")
    if "domain" in data:
        out["domain"] = data["domain"]
    if "scope" in data:
        import aws_sdk_codebuild.types.webhook_scope_type

        out["scope"] = (
            aws_sdk_codebuild.types.webhook_scope_type.deserialize_aws_json_1_1(
                data["scope"]
            )
        )
    else:
        raise DeserializationError("ScopeConfiguration.scope required")
    return out
