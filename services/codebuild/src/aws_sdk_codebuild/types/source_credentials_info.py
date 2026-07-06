"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceCredentialsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.auth_type
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.server_type
    import aws_sdk_codebuild.types.string


class SourceCredentialsInfo(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the token. </p>"""
    server_type: NotRequired["aws_sdk_codebuild.types.server_type.ServerType"]
    """<p> The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, GITLAB, GITLAB_SELF_MANAGED, or BITBUCKET. </p>"""
    auth_type: NotRequired["aws_sdk_codebuild.types.auth_type.AuthType"]
    """<p> The type of authentication used by the credentials. Valid options are OAUTH, BASIC_AUTH, PERSONAL_ACCESS_TOKEN, CODECONNECTIONS, or SECRETS_MANAGER. </p>"""
    resource: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The connection ARN if your authType is CODECONNECTIONS or SECRETS_MANAGER.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceCredentialsInfo) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "server_type" in value:
        import aws_sdk_codebuild.types.server_type

        out["serverType"] = aws_sdk_codebuild.types.server_type.serialize_aws_json_1_1(
            value["server_type"]
        )
    if "auth_type" in value:
        import aws_sdk_codebuild.types.auth_type

        out["authType"] = aws_sdk_codebuild.types.auth_type.serialize_aws_json_1_1(
            value["auth_type"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceCredentialsInfo:
    out: SourceCredentialsInfo = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "serverType" in data:
        import aws_sdk_codebuild.types.server_type

        out["server_type"] = (
            aws_sdk_codebuild.types.server_type.deserialize_aws_json_1_1(
                data["serverType"]
            )
        )
    if "authType" in data:
        import aws_sdk_codebuild.types.auth_type

        out["auth_type"] = aws_sdk_codebuild.types.auth_type.deserialize_aws_json_1_1(
            data["authType"]
        )
    if "resource" in data:
        out["resource"] = data["resource"]
    return out
