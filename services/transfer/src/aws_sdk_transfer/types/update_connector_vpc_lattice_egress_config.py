"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateConnectorVpcLatticeEgressConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.sftp_port
    import aws_sdk_transfer.types.vpc_lattice_resource_configuration_arn


class UpdateConnectorVpcLatticeEgressConfig(TypedDict, closed=True):
    resource_configuration_arn: NotRequired[
        "aws_sdk_transfer.types.vpc_lattice_resource_configuration_arn.VpcLatticeResourceConfigurationArn"
    ]
    """<p>Updated ARN of the VPC_LATTICE Resource Configuration. Use this to change the target SFTP server location or modify the network path through the customer's VPC infrastructure.</p>"""
    port_number: NotRequired["aws_sdk_transfer.types.sftp_port.SftpPort"]
    """<p>Updated port number for SFTP connections through VPC_LATTICE. Change this if the target SFTP server port has been modified or if connecting to a different server endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectorVpcLatticeEgressConfig) -> dict:
    out: dict = {}
    if "resource_configuration_arn" in value:
        out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    if "port_number" in value:
        out["PortNumber"] = value["port_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectorVpcLatticeEgressConfig:
    out: UpdateConnectorVpcLatticeEgressConfig = {}  # type: ignore[typeddict-item]
    if "ResourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    if "PortNumber" in data:
        out["port_number"] = data["PortNumber"]
    return out
