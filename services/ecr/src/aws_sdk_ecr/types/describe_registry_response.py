"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.replication_configuration


class DescribeRegistryResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    replication_configuration: NotRequired[
        "aws_sdk_ecr.types.replication_configuration.ReplicationConfiguration"
    ]
    """<p>The replication configuration for the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegistryResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "replication_configuration" in value:
        import aws_sdk_ecr.types.replication_configuration

        out["replicationConfiguration"] = (
            aws_sdk_ecr.types.replication_configuration.serialize_aws_json_1_1(
                value["replication_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegistryResponse:
    out: DescribeRegistryResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "replicationConfiguration" in data:
        import aws_sdk_ecr.types.replication_configuration

        out["replication_configuration"] = (
            aws_sdk_ecr.types.replication_configuration.deserialize_aws_json_1_1(
                data["replicationConfiguration"]
            )
        )
    return out
