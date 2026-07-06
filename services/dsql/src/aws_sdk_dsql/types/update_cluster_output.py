"""Generated from Smithy shape ``com.amazonaws.dsql#UpdateClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_arn
    import aws_sdk_dsql.types.cluster_creation_time
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.cluster_status


class UpdateClusterOutput(TypedDict, closed=True):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster to update.</p>"""
    arn: "aws_sdk_dsql.types.cluster_arn.ClusterArn"
    """<p>The ARN of the updated cluster.</p>"""
    status: "aws_sdk_dsql.types.cluster_status.ClusterStatus"
    """<p>The status of the updated cluster.</p>"""
    creation_time: "aws_sdk_dsql.types.cluster_creation_time.ClusterCreationTime"
    """<p>The time of when the cluster was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["arn"] = value["arn"]
    import aws_sdk_dsql.types.cluster_status

    out["status"] = aws_sdk_dsql.types.cluster_status.serialize_json(value["status"])
    import aws_sdk_dsql.types.cluster_creation_time

    out["creationTime"] = aws_sdk_dsql.types.cluster_creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateClusterOutput:
    out: UpdateClusterOutput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("UpdateClusterOutput.identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateClusterOutput.arn required")
    if "status" in data:
        import aws_sdk_dsql.types.cluster_status

        out["status"] = aws_sdk_dsql.types.cluster_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateClusterOutput.status required")
    if "creationTime" in data:
        import aws_sdk_dsql.types.cluster_creation_time

        out["creation_time"] = (
            aws_sdk_dsql.types.cluster_creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("UpdateClusterOutput.creation_time required")
    return out
