"""Generated from Smithy shape ``com.amazonaws.emr#GetOnClusterAppUIPresignedURLOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.xml_string


class GetOnClusterAppUIPresignedURLOutput(TypedDict):
    presigned_url_ready: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Used to determine if the presigned URL is ready.</p>"""
    presigned_url: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The cluster's generated presigned URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOnClusterAppUIPresignedURLOutput) -> dict:
    out: dict = {}
    if "presigned_url_ready" in value:
        out["PresignedURLReady"] = value["presigned_url_ready"]
    if "presigned_url" in value:
        out["PresignedURL"] = value["presigned_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOnClusterAppUIPresignedURLOutput:
    out: GetOnClusterAppUIPresignedURLOutput = {}  # type: ignore[typeddict-item]
    if "PresignedURLReady" in data:
        out["presigned_url_ready"] = data["PresignedURLReady"]
    if "PresignedURL" in data:
        out["presigned_url"] = data["PresignedURL"]
    return out
