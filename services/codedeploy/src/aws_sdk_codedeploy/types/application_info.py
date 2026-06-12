"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_id
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.boolean
    import aws_sdk_codedeploy.types.compute_platform
    import aws_sdk_codedeploy.types.git_hub_account_token_name
    import aws_sdk_codedeploy.types.timestamp


class ApplicationInfo(TypedDict):
    application_id: NotRequired["aws_sdk_codedeploy.types.application_id.ApplicationId"]
    """<p>The application ID.</p>"""
    application_name: NotRequired[
        "aws_sdk_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The application name.</p>"""
    create_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>The time at which the application was created.</p>"""
    linked_to_git_hub: "aws_sdk_codedeploy.types.boolean.Boolean"
    """<p>True if the user has authenticated with GitHub for the specified application. Otherwise, false.</p>"""
    git_hub_account_name: NotRequired[
        "aws_sdk_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
    ]
    """<p>The name for a connection to a GitHub account.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for deployment of the application (<code>Lambda</code> or <code>Server</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationInfo) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "create_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["createTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    out["linkedToGitHub"] = value.get("linked_to_git_hub", False)
    if "git_hub_account_name" in value:
        out["gitHubAccountName"] = value["git_hub_account_name"]
    if "compute_platform" in value:
        import aws_sdk_codedeploy.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationInfo:
    out: ApplicationInfo = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "createTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["create_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["createTime"]
            )
        )
    if "linkedToGitHub" in data:
        out["linked_to_git_hub"] = data["linkedToGitHub"]
    else:
        out["linked_to_git_hub"] = False
    if "gitHubAccountName" in data:
        out["git_hub_account_name"] = data["gitHubAccountName"]
    if "computePlatform" in data:
        import aws_sdk_codedeploy.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    return out
