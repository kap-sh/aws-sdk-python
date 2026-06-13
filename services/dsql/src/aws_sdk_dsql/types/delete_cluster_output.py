"""Generated from Smithy shape ``com.amazonaws.dsql#DeleteClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_arn
    import aws_sdk_dsql.types.cluster_creation_time
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.cluster_status


class DeleteClusterOutput(TypedDict):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the deleted cluster.</p>"""
    arn: "aws_sdk_dsql.types.cluster_arn.ClusterArn"
    """<p>The ARN of the deleted cluster.</p>"""
    status: "aws_sdk_dsql.types.cluster_status.ClusterStatus"
    """<p>The status of the cluster.</p>"""
    creation_time: "aws_sdk_dsql.types.cluster_creation_time.ClusterCreationTime"
    """<p>The time of when the cluster was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterOutput) -> dict:
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


def deserialize_json(data: dict) -> DeleteClusterOutput:
    out: DeleteClusterOutput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteClusterOutput.identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteClusterOutput.arn required")
    if "status" in data:
        import aws_sdk_dsql.types.cluster_status

        out["status"] = aws_sdk_dsql.types.cluster_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteClusterOutput.status required")
    if "creationTime" in data:
        import aws_sdk_dsql.types.cluster_creation_time

        out["creation_time"] = (
            aws_sdk_dsql.types.cluster_creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("DeleteClusterOutput.creation_time required")
    return out
