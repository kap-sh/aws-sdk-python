"""Generated from Smithy shape ``com.amazonaws.eks#CapabilitySummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.capability_status
    import aws_sdk_eks.types.capability_type
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.timestamp


class CapabilitySummary(TypedDict):
    capability_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The unique name of the capability within the cluster.</p>"""
    arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capability.</p>"""
    type: NotRequired["aws_sdk_eks.types.capability_type.CapabilityType"]
    """<p>The type of capability. Valid values are <code>ACK</code>, <code>ARGOCD</code>, or <code>KRO</code>.</p>"""
    status: NotRequired["aws_sdk_eks.types.capability_status.CapabilityStatus"]
    """<p>The current status of the capability.</p>"""
    version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The version of the capability software that is currently running.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the capability was created.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the capability was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilitySummary) -> dict:
    out: dict = {}
    if "capability_name" in value:
        out["capabilityName"] = value["capability_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_eks.types.capability_type

        out["type"] = aws_sdk_eks.types.capability_type.serialize_json(value["type"])
    if "status" in value:
        import aws_sdk_eks.types.capability_status

        out["status"] = aws_sdk_eks.types.capability_status.serialize_json(
            value["status"]
        )
    if "version" in value:
        out["version"] = value["version"]
    if "created_at" in value:
        import aws_sdk_eks.types.timestamp

        out["createdAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "modified_at" in value:
        import aws_sdk_eks.types.timestamp

        out["modifiedAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["modified_at"]
        )
    return out


def deserialize_json(data: dict) -> CapabilitySummary:
    out: CapabilitySummary = {}  # type: ignore[typeddict-item]
    if "capabilityName" in data:
        out["capability_name"] = data["capabilityName"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        import aws_sdk_eks.types.capability_type

        out["type"] = aws_sdk_eks.types.capability_type.deserialize_json(data["type"])
    if "status" in data:
        import aws_sdk_eks.types.capability_status

        out["status"] = aws_sdk_eks.types.capability_status.deserialize_json(
            data["status"]
        )
    if "version" in data:
        out["version"] = data["version"]
    if "createdAt" in data:
        import aws_sdk_eks.types.timestamp

        out["created_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "modifiedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["modified_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    return out
