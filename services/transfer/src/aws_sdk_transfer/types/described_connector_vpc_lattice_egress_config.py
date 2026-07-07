"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedConnectorVpcLatticeEgressConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.sftp_port
    import aws_sdk_transfer.types.vpc_lattice_resource_configuration_arn


class DescribedConnectorVpcLatticeEgressConfig(TypedDict, closed=True):
    resource_configuration_arn: "aws_sdk_transfer.types.vpc_lattice_resource_configuration_arn.VpcLatticeResourceConfigurationArn"
    """<p>ARN of the VPC_LATTICE Resource Configuration currently used by the connector. This Resource Configuration defines the network path to the SFTP server through the customer's VPC.</p>"""
    port_number: NotRequired["aws_sdk_transfer.types.sftp_port.SftpPort"]
    """<p>Port number currently configured for SFTP connections through VPC_LATTICE. Shows the port on which the connector attempts to connect to the target SFTP server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedConnectorVpcLatticeEgressConfig) -> dict:
    out: dict = {}
    out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    if "port_number" in value:
        out["PortNumber"] = value["port_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedConnectorVpcLatticeEgressConfig:
    out: DescribedConnectorVpcLatticeEgressConfig = {}  # type: ignore[typeddict-item]
    if "ResourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    else:
        raise DeserializationError(
            "DescribedConnectorVpcLatticeEgressConfig.resource_configuration_arn required"
        )
    if "PortNumber" in data:
        out["port_number"] = data["PortNumber"]
    return out
