"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateConfigurationBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.branch_name
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.component_configuration_map
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.version_created_by_source


class CreateConfigurationBundleRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    r"""<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    bundle_name: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
    """<p>The name for the configuration bundle. Names must be unique within your account.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
    ]
    """<p>The description for the configuration bundle.</p>"""
    components: "aws_sdk_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
    """<p>A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.</p>"""
    branch_name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
    ]
    """<p>The branch name for version tracking. Defaults to <code>mainline</code> if not specified.</p>"""
    commit_message: NotRequired["str"]
    """<p>A commit message describing the initial version of the configuration bundle.</p>"""
    created_by: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
    ]
    """<p>The source that created this version, including the source name and optional ARN.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationBundleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["bundleName"] = value["bundle_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.component_configuration_map

    out["components"] = (
        aws_sdk_bedrock_agentcore_control.types.component_configuration_map.serialize_json(
            value["components"]
        )
    )
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    if "created_by" in value:
        import aws_sdk_bedrock_agentcore_control.types.version_created_by_source

        out["createdBy"] = (
            aws_sdk_bedrock_agentcore_control.types.version_created_by_source.serialize_json(
                value["created_by"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateConfigurationBundleRequest:
    out: CreateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "bundleName" in data:
        out["bundle_name"] = data["bundleName"]
    else:
        raise DeserializationError(
            "CreateConfigurationBundleRequest.bundle_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "components" in data:
        import aws_sdk_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            aws_sdk_bedrock_agentcore_control.types.component_configuration_map.deserialize_json(
                data["components"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationBundleRequest.components required"
        )
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    if "createdBy" in data:
        import aws_sdk_bedrock_agentcore_control.types.version_created_by_source

        out["created_by"] = (
            aws_sdk_bedrock_agentcore_control.types.version_created_by_source.deserialize_json(
                data["createdBy"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
