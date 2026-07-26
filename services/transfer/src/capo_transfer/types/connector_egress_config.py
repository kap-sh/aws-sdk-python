"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorEgressConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_transfer.types.connector_vpc_lattice_egress_config


class _ConnectorEgressConfig_VpcLattice(TypedDict, closed=True):
    VpcLattice: "capo_transfer.types.connector_vpc_lattice_egress_config.ConnectorVpcLatticeEgressConfig"


ConnectorEgressConfig: TypeAlias = _ConnectorEgressConfig_VpcLattice


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorEgressConfig) -> dict:
    if "VpcLattice" in value:
        import capo_transfer.types.connector_vpc_lattice_egress_config

        return {
            "VpcLattice": capo_transfer.types.connector_vpc_lattice_egress_config.serialize_aws_json_1_1(
                value["VpcLattice"]
            )
        }
    else:
        raise SerializationError("ConnectorEgressConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ConnectorEgressConfig:
    if "VpcLattice" in data:
        import capo_transfer.types.connector_vpc_lattice_egress_config

        return {
            "VpcLattice": capo_transfer.types.connector_vpc_lattice_egress_config.deserialize_aws_json_1_1(
                data["VpcLattice"]
            )
        }
    else:
        raise DeserializationError("ConnectorEgressConfig: no recognized variant key")
