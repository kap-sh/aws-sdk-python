"""Generated from Smithy shape ``com.amazonaws.sagemaker#UiTemplateInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.template_content_sha256
    import aws_sdk_sagemaker.types.template_url


class UiTemplateInfo(TypedDict):
    url: NotRequired["aws_sdk_sagemaker.types.template_url.TemplateUrl"]
    """<p>The URL for the user interface template.</p>"""
    content_sha256: NotRequired[
        "aws_sdk_sagemaker.types.template_content_sha256.TemplateContentSha256"
    ]
    """<p>The SHA-256 digest of the contents of the template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UiTemplateInfo) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "content_sha256" in value:
        out["ContentSha256"] = value["content_sha256"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UiTemplateInfo:
    out: UiTemplateInfo = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "ContentSha256" in data:
        out["content_sha256"] = data["ContentSha256"]
    return out
