"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcBlockPublicAccessOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_options


class DescribeVpcBlockPublicAccessOptionsResult(TypedDict):
    vpc_block_public_access_options: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_options.VpcBlockPublicAccessOptions"
    ]
    """<p>Details related to the options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcBlockPublicAccessOptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_block_public_access_options" in value:
        import aws_sdk_ec2.types.vpc_block_public_access_options

        aws_sdk_ec2.types.vpc_block_public_access_options.serialize_ec2_query(
            value["vpc_block_public_access_options"],
            pairs,
            f"{prefix}.VpcBlockPublicAccessOptions",
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcBlockPublicAccessOptionsResult:
    out: DescribeVpcBlockPublicAccessOptionsResult = {}  # type: ignore[typeddict-item]
    child_vpc_block_public_access_options = el.find("VpcBlockPublicAccessOptions")
    if child_vpc_block_public_access_options is not None:
        import aws_sdk_ec2.types.vpc_block_public_access_options

        out["vpc_block_public_access_options"] = (
            aws_sdk_ec2.types.vpc_block_public_access_options.deserialize_ec2_query(
                child_vpc_block_public_access_options
            )
        )
    return out
