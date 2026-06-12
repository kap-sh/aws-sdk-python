"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DataArtifact``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_marketplace_discovery.errors import DeserializationError

class DataArtifact(TypedDict):
    description: NotRequired["str"]
    """<p>A description of the data artifact.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the data artifact.</p>"""
    resource_type: "str"
    """<p>The type of the data artifact resource.</p>"""
    data_classification: "str"
    """<p>The classification of sensitive data contained in the dataset.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DataArtifact) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    out["resourceType"] = value["resource_type"]
    out["dataClassification"] = value["data_classification"]
    return out


def deserialize_json(data: dict) -> DataArtifact:
    out: DataArtifact = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("DataArtifact.resource_type required")
    if "dataClassification" in data:
        out["data_classification"] = data["dataClassification"]
    else:
        raise DeserializationError("DataArtifact.data_classification required")
    return out