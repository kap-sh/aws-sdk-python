"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalySourceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.anomaly_source
    import aws_sdk_devops_guru.types.resource_name
    import aws_sdk_devops_guru.types.resource_type


class AnomalySourceMetadata(TypedDict, closed=True):
    source: NotRequired["aws_sdk_devops_guru.types.anomaly_source.AnomalySource"]
    """<p>The source of the anomaly.</p>"""
    source_resource_name: NotRequired[
        "aws_sdk_devops_guru.types.resource_name.ResourceName"
    ]
    """<p>The name of the anomaly's resource.</p>"""
    source_resource_type: NotRequired[
        "aws_sdk_devops_guru.types.resource_type.ResourceType"
    ]
    """<p>The anomaly's resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalySourceMetadata) -> dict:
    out: dict = {}
    if "source" in value:
        out["Source"] = value["source"]
    if "source_resource_name" in value:
        out["SourceResourceName"] = value["source_resource_name"]
    if "source_resource_type" in value:
        out["SourceResourceType"] = value["source_resource_type"]
    return out


def deserialize_json(data: dict) -> AnomalySourceMetadata:
    out: AnomalySourceMetadata = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        out["source"] = data["Source"]
    if "SourceResourceName" in data:
        out["source_resource_name"] = data["SourceResourceName"]
    if "SourceResourceType" in data:
        out["source_resource_type"] = data["SourceResourceType"]
    return out
