"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlExclusions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control_exclusion

VpcEncryptionControlExclusions = TypedDict(
    "VpcEncryptionControlExclusions",
    {
        "internet_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "egress_only_internet_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "nat_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "virtual_private_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "vpc_peering": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "lambda": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "vpc_lattice": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "elastic_file_system": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
    },
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControlExclusions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "internet_gateway" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["internet_gateway"], pairs, f"{prefix}.InternetGateway"
        )
    if "egress_only_internet_gateway" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["egress_only_internet_gateway"],
            pairs,
            f"{prefix}.EgressOnlyInternetGateway",
        )
    if "nat_gateway" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["nat_gateway"], pairs, f"{prefix}.NatGateway"
        )
    if "virtual_private_gateway" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["virtual_private_gateway"], pairs, f"{prefix}.VirtualPrivateGateway"
        )
    if "vpc_peering" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["vpc_peering"], pairs, f"{prefix}.VpcPeering"
        )
    if "lambda" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["lambda"], pairs, f"{prefix}.Lambda"
        )
    if "vpc_lattice" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["vpc_lattice"], pairs, f"{prefix}.VpcLattice"
        )
    if "elastic_file_system" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        aws_sdk_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["elastic_file_system"], pairs, f"{prefix}.ElasticFileSystem"
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlExclusions:
    out: VpcEncryptionControlExclusions = {}  # type: ignore[typeddict-item]
    child_internet_gateway = el.find("InternetGateway")
    if child_internet_gateway is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["internet_gateway"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_internet_gateway
            )
        )
    child_egress_only_internet_gateway = el.find("EgressOnlyInternetGateway")
    if child_egress_only_internet_gateway is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["egress_only_internet_gateway"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_egress_only_internet_gateway
            )
        )
    child_nat_gateway = el.find("NatGateway")
    if child_nat_gateway is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["nat_gateway"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_nat_gateway
            )
        )
    child_virtual_private_gateway = el.find("VirtualPrivateGateway")
    if child_virtual_private_gateway is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["virtual_private_gateway"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_virtual_private_gateway
            )
        )
    child_vpc_peering = el.find("VpcPeering")
    if child_vpc_peering is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["vpc_peering"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_vpc_peering
            )
        )
    child_lambda = el.find("Lambda")
    if child_lambda is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["lambda"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_lambda
            )
        )
    child_vpc_lattice = el.find("VpcLattice")
    if child_vpc_lattice is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["vpc_lattice"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_vpc_lattice
            )
        )
    child_elastic_file_system = el.find("ElasticFileSystem")
    if child_elastic_file_system is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusion

        out["elastic_file_system"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_elastic_file_system
            )
        )
    return out
