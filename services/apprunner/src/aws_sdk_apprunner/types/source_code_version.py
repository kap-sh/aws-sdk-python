"""Generated from Smithy shape ``com.amazonaws.apprunner#SourceCodeVersion``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.source_code_version_type
    import aws_sdk_apprunner.types.string


class SourceCodeVersion(TypedDict):
    type: "aws_sdk_apprunner.types.source_code_version_type.SourceCodeVersionType"
    """<p>The type of version identifier.</p> <p>For a git-based repository, branches represent versions.</p>"""
    value: "aws_sdk_apprunner.types.string.String"
    """<p>A source code version.</p> <p>For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceCodeVersion) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.source_code_version_type

    out["Type"] = (
        aws_sdk_apprunner.types.source_code_version_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceCodeVersion:
    out: SourceCodeVersion = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_apprunner.types.source_code_version_type

        out["type"] = (
            aws_sdk_apprunner.types.source_code_version_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("SourceCodeVersion.type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("SourceCodeVersion.value required")
    return out
