"""Generated from Smithy shape ``com.amazonaws.ecr#ImageReplicationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.region
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_error
    import capo_ecr.types.replication_status


class ImageReplicationStatus(TypedDict, closed=True):
    region: NotRequired["capo_ecr.types.region.Region"]
    """<p>The destination Region for the image replication.</p>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to which the image belongs.</p>"""
    status: NotRequired["capo_ecr.types.replication_status.ReplicationStatus"]
    """<p>The image replication status.</p>"""
    failure_code: NotRequired["capo_ecr.types.replication_error.ReplicationError"]
    """<p>The failure code for a replication that has failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageReplicationStatus) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "status" in value:
        import capo_ecr.types.replication_status

        out["status"] = capo_ecr.types.replication_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageReplicationStatus:
    out: ImageReplicationStatus = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "status" in data:
        import capo_ecr.types.replication_status

        out["status"] = capo_ecr.types.replication_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    return out
