"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateConnectorEgressConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.update_connector_vpc_lattice_egress_config


class _UpdateConnectorEgressConfig_VpcLattice(TypedDict):
    VpcLattice: "aws_sdk_transfer.types.update_connector_vpc_lattice_egress_config.UpdateConnectorVpcLatticeEgressConfig"


UpdateConnectorEgressConfig: TypeAlias = _UpdateConnectorEgressConfig_VpcLattice


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectorEgressConfig) -> dict:
    if "VpcLattice" in value:
        import aws_sdk_transfer.types.update_connector_vpc_lattice_egress_config

        return {
            "VpcLattice": aws_sdk_transfer.types.update_connector_vpc_lattice_egress_config.serialize_aws_json_1_1(
                value["VpcLattice"]
            )
        }
    else:
        raise SerializationError("UpdateConnectorEgressConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectorEgressConfig:
    if "VpcLattice" in data:
        import aws_sdk_transfer.types.update_connector_vpc_lattice_egress_config

        return {
            "VpcLattice": aws_sdk_transfer.types.update_connector_vpc_lattice_egress_config.deserialize_aws_json_1_1(
                data["VpcLattice"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateConnectorEgressConfig: no recognized variant key"
        )
