"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_inspector2.types.cluster_metadata


class ClusterDetails(TypedDict):
    last_in_use: "datetime.datetime"
    """<p>The last timestamp when Amazon Inspector recorded the image in use in the task or pod in the cluster.</p>"""
    running_unit_count: NotRequired["int"]
    """<p>The number of tasks or pods where an image was running on the cluster.</p>"""
    stopped_unit_count: NotRequired["int"]
    """<p>The number of tasks or pods where an image was stopped on the cluster in the last 24 hours.</p>"""
    cluster_metadata: "aws_sdk_inspector2.types.cluster_metadata.ClusterMetadata"


# --- restJson1 ser/de ---
def serialize_json(value: ClusterDetails) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types._prelude.timestamp

    out["lastInUse"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
        value["last_in_use"]
    )
    if "running_unit_count" in value:
        out["runningUnitCount"] = value["running_unit_count"]
    if "stopped_unit_count" in value:
        out["stoppedUnitCount"] = value["stopped_unit_count"]
    import aws_sdk_inspector2.types.cluster_metadata

    out["clusterMetadata"] = aws_sdk_inspector2.types.cluster_metadata.serialize_json(
        value["cluster_metadata"]
    )
    return out


def deserialize_json(data: dict) -> ClusterDetails:
    out: ClusterDetails = {}  # type: ignore[typeddict-item]
    if "lastInUse" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["last_in_use"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastInUse"]
            )
        )
    else:
        raise DeserializationError("ClusterDetails.last_in_use required")
    if "runningUnitCount" in data:
        out["running_unit_count"] = data["runningUnitCount"]
    if "stoppedUnitCount" in data:
        out["stopped_unit_count"] = data["stoppedUnitCount"]
    if "clusterMetadata" in data:
        import aws_sdk_inspector2.types.cluster_metadata

        out["cluster_metadata"] = (
            aws_sdk_inspector2.types.cluster_metadata.deserialize_json(
                data["clusterMetadata"]
            )
        )
    else:
        raise DeserializationError("ClusterDetails.cluster_metadata required")
    return out
