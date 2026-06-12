"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorVpcLatticeEgressConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.sftp_port
    import aws_sdk_transfer.types.vpc_lattice_resource_configuration_arn


class ConnectorVpcLatticeEgressConfig(TypedDict):
    resource_configuration_arn: "aws_sdk_transfer.types.vpc_lattice_resource_configuration_arn.VpcLatticeResourceConfigurationArn"
    """<p>ARN of the VPC_LATTICE Resource Configuration that defines the target SFTP server location. Must point to a valid Resource Configuration in the customer's VPC with appropriate network connectivity to the SFTP server.</p>"""
    port_number: NotRequired["aws_sdk_transfer.types.sftp_port.SftpPort"]
    """<p>Port number for connecting to the SFTP server through VPC_LATTICE. Defaults to 22 if not specified. Must match the port on which the target SFTP server is listening.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorVpcLatticeEgressConfig) -> dict:
    out: dict = {}
    out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    if "port_number" in value:
        out["PortNumber"] = value["port_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorVpcLatticeEgressConfig:
    out: ConnectorVpcLatticeEgressConfig = {}  # type: ignore[typeddict-item]
    if "ResourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    else:
        raise DeserializationError(
            "ConnectorVpcLatticeEgressConfig.resource_configuration_arn required"
        )
    if "PortNumber" in data:
        out["port_number"] = data["PortNumber"]
    return out
