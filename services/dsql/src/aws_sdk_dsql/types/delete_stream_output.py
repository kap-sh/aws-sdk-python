"""Generated from Smithy shape ``com.amazonaws.dsql#DeleteStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.stream_arn
    import aws_sdk_dsql.types.stream_creation_time
    import aws_sdk_dsql.types.stream_id
    import aws_sdk_dsql.types.stream_status


class DeleteStreamOutput(TypedDict, closed=True):
    cluster_identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for the deleted stream.</p>"""
    stream_identifier: "aws_sdk_dsql.types.stream_id.StreamId"
    """<p>The ID of the deleted stream.</p>"""
    arn: "aws_sdk_dsql.types.stream_arn.StreamArn"
    """<p>The ARN of the deleted stream.</p>"""
    status: "aws_sdk_dsql.types.stream_status.StreamStatus"
    """<p>The status of the stream.</p>"""
    creation_time: "aws_sdk_dsql.types.stream_creation_time.StreamCreationTime"
    """<p>The time when the stream was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamOutput) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["streamIdentifier"] = value["stream_identifier"]
    out["arn"] = value["arn"]
    import aws_sdk_dsql.types.stream_status

    out["status"] = aws_sdk_dsql.types.stream_status.serialize_json(value["status"])
    import aws_sdk_dsql.types.stream_creation_time

    out["creationTime"] = aws_sdk_dsql.types.stream_creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> DeleteStreamOutput:
    out: DeleteStreamOutput = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("DeleteStreamOutput.cluster_identifier required")
    if "streamIdentifier" in data:
        out["stream_identifier"] = data["streamIdentifier"]
    else:
        raise DeserializationError("DeleteStreamOutput.stream_identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteStreamOutput.arn required")
    if "status" in data:
        import aws_sdk_dsql.types.stream_status

        out["status"] = aws_sdk_dsql.types.stream_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteStreamOutput.status required")
    if "creationTime" in data:
        import aws_sdk_dsql.types.stream_creation_time

        out["creation_time"] = aws_sdk_dsql.types.stream_creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("DeleteStreamOutput.creation_time required")
    return out
