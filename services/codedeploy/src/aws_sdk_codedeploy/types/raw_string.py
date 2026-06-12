"""Generated from Smithy shape ``com.amazonaws.codedeploy#RawString``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.raw_string_content
    import aws_sdk_codedeploy.types.raw_string_sha256


class RawString(TypedDict):
    content: NotRequired["aws_sdk_codedeploy.types.raw_string_content.RawStringContent"]
    """<p>The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.</p>"""
    sha256: NotRequired["aws_sdk_codedeploy.types.raw_string_sha256.RawStringSha256"]
    """<p>The SHA256 hash value of the revision content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RawString) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RawString:
    out: RawString = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    if "sha256" in data:
        out["sha256"] = data["sha256"]
    return out
