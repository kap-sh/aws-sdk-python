"""Generated from Smithy shape ``com.amazonaws.dsql#StreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dsql.types.cluster_id
    import capo_dsql.types.stream_arn
    import capo_dsql.types.stream_creation_time
    import capo_dsql.types.stream_id
    import capo_dsql.types.stream_status


class StreamSummary(TypedDict, closed=True):
    cluster_identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster.</p>"""
    stream_identifier: "capo_dsql.types.stream_id.StreamId"
    """<p>The ID of the stream.</p>"""
    arn: "capo_dsql.types.stream_arn.StreamArn"
    """<p>The ARN of the stream.</p>"""
    creation_time: "capo_dsql.types.stream_creation_time.StreamCreationTime"
    """<p>The timestamp when the stream was created.</p>"""
    status: "capo_dsql.types.stream_status.StreamStatus"
    """<p>The current status of the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSummary) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["streamIdentifier"] = value["stream_identifier"]
    out["arn"] = value["arn"]
    import capo_dsql.types.stream_creation_time

    out["creationTime"] = capo_dsql.types.stream_creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_dsql.types.stream_status

    out["status"] = capo_dsql.types.stream_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> StreamSummary:
    out: StreamSummary = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("StreamSummary.cluster_identifier required")
    if "streamIdentifier" in data:
        out["stream_identifier"] = data["streamIdentifier"]
    else:
        raise DeserializationError("StreamSummary.stream_identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StreamSummary.arn required")
    if "creationTime" in data:
        import capo_dsql.types.stream_creation_time

        out["creation_time"] = capo_dsql.types.stream_creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("StreamSummary.creation_time required")
    if "status" in data:
        import capo_dsql.types.stream_status

        out["status"] = capo_dsql.types.stream_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("StreamSummary.status required")
    return out
