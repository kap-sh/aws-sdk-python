"""Generated from Smithy shape ``com.amazonaws.dsql#CreateStreamOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dsql.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.stream_arn
    import aws_sdk_dsql.types.stream_creation_time
    import aws_sdk_dsql.types.stream_format
    import aws_sdk_dsql.types.stream_id
    import aws_sdk_dsql.types.stream_ordering
    import aws_sdk_dsql.types.stream_status

class CreateStreamOutput(TypedDict):
    cluster_identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for the created stream.</p>"""
    stream_identifier: "aws_sdk_dsql.types.stream_id.StreamId"
    """<p>The ID of the created stream.</p>"""
    arn: "aws_sdk_dsql.types.stream_arn.StreamArn"
    """<p>The ARN of the created stream.</p>"""
    status: "aws_sdk_dsql.types.stream_status.StreamStatus"
    """<p>The status of the created stream.</p>"""
    creation_time: "aws_sdk_dsql.types.stream_creation_time.StreamCreationTime"
    """<p>The time when created the stream.</p>"""
    ordering: "aws_sdk_dsql.types.stream_ordering.StreamOrdering"
    """<p>The ordering mode of the created stream.</p>"""
    format: "aws_sdk_dsql.types.stream_format.StreamFormat"
    """<p>The format of the created stream records.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamOutput) -> dict:
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
    return out


def deserialize_json(data: dict) -> CreateStreamOutput:
    out: CreateStreamOutput = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("CreateStreamOutput.cluster_identifier required")
    if "streamIdentifier" in data:
        out["stream_identifier"] = data["streamIdentifier"]
    else:
        raise DeserializationError("CreateStreamOutput.stream_identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateStreamOutput.arn required")
    if "status" in data:
        import aws_sdk_dsql.types.stream_status
        out["status"] = aws_sdk_dsql.types.stream_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateStreamOutput.status required")
    if "creationTime" in data:
        import aws_sdk_dsql.types.stream_creation_time
        out["creation_time"] = aws_sdk_dsql.types.stream_creation_time.deserialize_json(data["creationTime"])
    else:
        raise DeserializationError("CreateStreamOutput.creation_time required")
    if "ordering" in data:
        import aws_sdk_dsql.types.stream_ordering
        out["ordering"] = aws_sdk_dsql.types.stream_ordering.deserialize_json(data["ordering"])
    else:
        raise DeserializationError("CreateStreamOutput.ordering required")
    if "format" in data:
        import aws_sdk_dsql.types.stream_format
        out["format"] = aws_sdk_dsql.types.stream_format.deserialize_json(data["format"])
    else:
        raise DeserializationError("CreateStreamOutput.format required")
    return out