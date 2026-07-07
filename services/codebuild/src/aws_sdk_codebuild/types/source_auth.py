"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceAuth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.source_auth_type
    import aws_sdk_codebuild.types.string


class SourceAuth(TypedDict, closed=True):
    type: "aws_sdk_codebuild.types.source_auth_type.SourceAuthType"
    """<p>The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.</p>"""
    resource: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The resource value that applies to the specified authorization type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAuth) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.source_auth_type

    out["type"] = aws_sdk_codebuild.types.source_auth_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceAuth:
    out: SourceAuth = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_codebuild.types.source_auth_type

        out["type"] = aws_sdk_codebuild.types.source_auth_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("SourceAuth.type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    return out
