"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input
    import aws_sdk_ec2.types.vpc_encryption_control_mode


class VpcEncryptionControlConfiguration(TypedDict):
    mode: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_mode.VpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the VPC Encryption Control configuration.</p>"""
    internet_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude internet gateway traffic from encryption enforcement.</p>"""
    egress_only_internet_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement.</p>"""
    nat_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude NAT gateway traffic from encryption enforcement.</p>"""
    virtual_private_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude virtual private gateway traffic from encryption enforcement.</p>"""
    vpc_peering_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude VPC peering connection traffic from encryption enforcement.</p>"""
    lambda_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Lambda function traffic from encryption enforcement.</p>"""
    vpc_lattice_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude VPC Lattice traffic from encryption enforcement.</p>"""
    elastic_file_system_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Elastic File System traffic from encryption enforcement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControlConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "mode" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_mode

        aws_sdk_ec2.types.vpc_encryption_control_mode.serialize_ec2_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "internet_gateway_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["internet_gateway_exclusion"],
            pairs,
            f"{prefix}.InternetGatewayExclusion",
        )
    if "egress_only_internet_gateway_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["egress_only_internet_gateway_exclusion"],
            pairs,
            f"{prefix}.EgressOnlyInternetGatewayExclusion",
        )
    if "nat_gateway_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["nat_gateway_exclusion"], pairs, f"{prefix}.NatGatewayExclusion"
        )
    if "virtual_private_gateway_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["virtual_private_gateway_exclusion"],
            pairs,
            f"{prefix}.VirtualPrivateGatewayExclusion",
        )
    if "vpc_peering_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["vpc_peering_exclusion"], pairs, f"{prefix}.VpcPeeringExclusion"
        )
    if "lambda_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["lambda_exclusion"], pairs, f"{prefix}.LambdaExclusion"
        )
    if "vpc_lattice_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["vpc_lattice_exclusion"], pairs, f"{prefix}.VpcLatticeExclusion"
        )
    if "elastic_file_system_exclusion" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["elastic_file_system_exclusion"],
            pairs,
            f"{prefix}.ElasticFileSystemExclusion",
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlConfiguration:
    out: VpcEncryptionControlConfiguration = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_mode

        out["mode"] = (
            aws_sdk_ec2.types.vpc_encryption_control_mode.deserialize_ec2_query(
                child_mode
            )
        )
    child_internet_gateway_exclusion = el.find("InternetGatewayExclusion")
    if child_internet_gateway_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["internet_gateway_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_internet_gateway_exclusion
            )
        )
    child_egress_only_internet_gateway_exclusion = el.find(
        "EgressOnlyInternetGatewayExclusion"
    )
    if child_egress_only_internet_gateway_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["egress_only_internet_gateway_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_egress_only_internet_gateway_exclusion
            )
        )
    child_nat_gateway_exclusion = el.find("NatGatewayExclusion")
    if child_nat_gateway_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["nat_gateway_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_nat_gateway_exclusion
            )
        )
    child_virtual_private_gateway_exclusion = el.find("VirtualPrivateGatewayExclusion")
    if child_virtual_private_gateway_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["virtual_private_gateway_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_virtual_private_gateway_exclusion
            )
        )
    child_vpc_peering_exclusion = el.find("VpcPeeringExclusion")
    if child_vpc_peering_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["vpc_peering_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_vpc_peering_exclusion
            )
        )
    child_lambda_exclusion = el.find("LambdaExclusion")
    if child_lambda_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["lambda_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_lambda_exclusion
            )
        )
    child_vpc_lattice_exclusion = el.find("VpcLatticeExclusion")
    if child_vpc_lattice_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["vpc_lattice_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_vpc_lattice_exclusion
            )
        )
    child_elastic_file_system_exclusion = el.find("ElasticFileSystemExclusion")
    if child_elastic_file_system_exclusion is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input

        out["elastic_file_system_exclusion"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_elastic_file_system_exclusion
            )
        )
    return out
