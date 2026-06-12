"""Generated from Smithy shape ``com.amazonaws.dsql#GetStreamOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dsql.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.status_reason
    import aws_sdk_dsql.types.stream_arn
    import aws_sdk_dsql.types.stream_creation_time
    import aws_sdk_dsql.types.stream_format
    import aws_sdk_dsql.types.stream_id
    import aws_sdk_dsql.types.stream_ordering
    import aws_sdk_dsql.types.stream_status
    import aws_sdk_dsql.types.tag_map
    import aws_sdk_dsql.types.target_definition

class GetStreamOutput(TypedDict):
    cluster_identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for the retrieved stream.</p>"""
    stream_identifier: "aws_sdk_dsql.types.stream_id.StreamId"
    """<p>The ID of the retrieved stream.</p>"""
    arn: "aws_sdk_dsql.types.stream_arn.StreamArn"
    """<p>The ARN of the retrieved stream.</p>"""
    status: "aws_sdk_dsql.types.stream_status.StreamStatus"
    """<p>The current status of the retrieved stream.</p>"""
    creation_time: "aws_sdk_dsql.types.stream_creation_time.StreamCreationTime"
    """<p>The time when the stream was created.</p>"""
    ordering: "aws_sdk_dsql.types.stream_ordering.StreamOrdering"
    """<p>The ordering mode of the stream.</p>"""
    format: "aws_sdk_dsql.types.stream_format.StreamFormat"
    """<p>The format of the stream records.</p>"""
    target_definition: NotRequired["aws_sdk_dsql.types.target_definition.TargetDefinition"]
    """<p>The target definition for the stream destination.</p>"""
    status_reason: NotRequired["aws_sdk_dsql.types.status_reason.StatusReason"]
    """<p>Stream status reason with error code and timestamp (if applicable).</p>"""
    tags: NotRequired["aws_sdk_dsql.types.tag_map.TagMap"]
    """<p>A map of tags associated with the stream.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetStreamOutput) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["streamIdentifier"] = value["stream_identifier"]
    out["arn"] = value["arn"]
    import aws_sdk_dsql.types.stream_status
    out["status"] = aws_sdk_dsql.types.stream_status.serialize_json(value["status"])
    import aws_sdk_dsql.types.stream_creation_time
    out["creationTime"] = aws_sdk_dsql.types.stream_creation_time.serialize_json(value["creation_time"])
    import aws_sdk_dsql.types.stream_ordering
    out["ordering"] = aws_sdk_dsql.types.stream_ordering.serialize_json(value["ordering"])
    import aws_sdk_dsql.types.stream_format
    out["format"] = aws_sdk_dsql.types.stream_format.serialize_json(value["format"])
    if "target_definition" in value:
        import aws_sdk_dsql.types.target_definition
        out["targetDefinition"] = aws_sdk_dsql.types.target_definition.serialize_json(value["target_definition"])
    if "status_reason" in value:
        import aws_sdk_dsql.types.status_reason
        out["statusReason"] = aws_sdk_dsql.types.status_reason.serialize_json(value["status_reason"])
    if "tags" in value:
        import aws_sdk_dsql.types.tag_map
        out["tags"] = aws_sdk_dsql.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetStreamOutput:
    out: GetStreamOutput = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("GetStreamOutput.cluster_identifier required")
    if "streamIdentifier" in data:
        out["stream_identifier"] = data["streamIdentifier"]
    else:
        raise DeserializationError("GetStreamOutput.stream_identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetStreamOutput.arn required")
    if "status" in data:
        import aws_sdk_dsql.types.stream_status
        out["status"] = aws_sdk_dsql.types.stream_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetStreamOutput.status required")
    if "creationTime" in data:
        import aws_sdk_dsql.types.stream_creation_time
        out["creation_time"] = aws_sdk_dsql.types.stream_creation_time.deserialize_json(data["creationTime"])
    else:
        raise DeserializationError("GetStreamOutput.creation_time required")
    if "ordering" in data:
        import aws_sdk_dsql.types.stream_ordering
        out["ordering"] = aws_sdk_dsql.types.stream_ordering.deserialize_json(data["ordering"])
    else:
        raise DeserializationError("GetStreamOutput.ordering required")
    if "format" in data:
        import aws_sdk_dsql.types.stream_format
        out["format"] = aws_sdk_dsql.types.stream_format.deserialize_json(data["format"])
    else:
        raise DeserializationError("GetStreamOutput.format required")
    if "targetDefinition" in data:
        import aws_sdk_dsql.types.target_definition
        out["target_definition"] = aws_sdk_dsql.types.target_definition.deserialize_json(data["targetDefinition"])
    if "statusReason" in data:
        import aws_sdk_dsql.types.status_reason
        out["status_reason"] = aws_sdk_dsql.types.status_reason.deserialize_json(data["statusReason"])
    if "tags" in data:
        import aws_sdk_dsql.types.tag_map
        out["tags"] = aws_sdk_dsql.types.tag_map.deserialize_json(data["tags"])
    return out