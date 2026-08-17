"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_configuration


class DescribeRegistryResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    replication_configuration: NotRequired[
        "capo_ecr.types.replication_configuration.ReplicationConfiguration"
    ]
    """<p>The replication configuration for the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegistryResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "replication_configuration" in value:
        import capo_ecr.types.replication_configuration

        out["replicationConfiguration"] = (
            capo_ecr.types.replication_configuration.serialize_aws_json_1_1(
                value["replication_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegistryResponse:
    out: DescribeRegistryResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("replicationConfiguration") is not None:
        import capo_ecr.types.replication_configuration

        out["replication_configuration"] = (
            capo_ecr.types.replication_configuration.deserialize_aws_json_1_1(
                data["replicationConfiguration"]
            )
        )
    return out
