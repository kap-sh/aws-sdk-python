"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActionSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.source_uri
    import aws_sdk_sagemaker.types.string256


class ActionSource(TypedDict):
    source_uri: NotRequired["aws_sdk_sagemaker.types.source_uri.SourceUri"]
    """<p>The URI of the source.</p>"""
    source_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The type of the source.</p>"""
    source_id: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The ID of the source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionSource) -> dict:
    out: dict = {}
    if "source_uri" in value:
        out["SourceUri"] = value["source_uri"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionSource:
    out: ActionSource = {}  # type: ignore[typeddict-item]
    if "SourceUri" in data:
        out["source_uri"] = data["SourceUri"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    return out
