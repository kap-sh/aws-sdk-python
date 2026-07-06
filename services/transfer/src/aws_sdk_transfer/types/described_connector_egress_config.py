"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedConnectorEgressConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_connector_vpc_lattice_egress_config


class _DescribedConnectorEgressConfig_VpcLattice(TypedDict, closed=True):
    VpcLattice: "aws_sdk_transfer.types.described_connector_vpc_lattice_egress_config.DescribedConnectorVpcLatticeEgressConfig"


DescribedConnectorEgressConfig: TypeAlias = _DescribedConnectorEgressConfig_VpcLattice


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedConnectorEgressConfig) -> dict:
    if "VpcLattice" in value:
        import aws_sdk_transfer.types.described_connector_vpc_lattice_egress_config

        return {
            "VpcLattice": aws_sdk_transfer.types.described_connector_vpc_lattice_egress_config.serialize_aws_json_1_1(
                value["VpcLattice"]
            )
        }
    else:
        raise SerializationError("DescribedConnectorEgressConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DescribedConnectorEgressConfig:
    if "VpcLattice" in data:
        import aws_sdk_transfer.types.described_connector_vpc_lattice_egress_config

        return {
            "VpcLattice": aws_sdk_transfer.types.described_connector_vpc_lattice_egress_config.deserialize_aws_json_1_1(
                data["VpcLattice"]
            )
        }
    else:
        raise DeserializationError(
            "DescribedConnectorEgressConfig: no recognized variant key"
        )
