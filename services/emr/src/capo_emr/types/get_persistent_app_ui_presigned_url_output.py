"""Generated from Smithy shape ``com.amazonaws.emr#GetPersistentAppUIPresignedURLOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.xml_string


class GetPersistentAppUIPresignedURLOutput(TypedDict, closed=True):
    presigned_url_ready: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Used to determine if the presigned URL is ready.</p>"""
    presigned_url: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The returned presigned URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPersistentAppUIPresignedURLOutput) -> dict:
    out: dict = {}
    if "presigned_url_ready" in value:
        out["PresignedURLReady"] = value["presigned_url_ready"]
    if "presigned_url" in value:
        out["PresignedURL"] = value["presigned_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPersistentAppUIPresignedURLOutput:
    out: GetPersistentAppUIPresignedURLOutput = {}  # type: ignore[typeddict-item]
    if "PresignedURLReady" in data:
        out["presigned_url_ready"] = data["PresignedURLReady"]
    if "PresignedURL" in data:
        out["presigned_url"] = data["PresignedURL"]
    return out
