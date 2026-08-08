"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcBlockPublicAccessOptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_block_public_access_options


class ModifyVpcBlockPublicAccessOptionsResult(TypedDict, closed=True):
    vpc_block_public_access_options: NotRequired[
        "capo_ec2.types.vpc_block_public_access_options.VpcBlockPublicAccessOptions"
    ]
    """<p>Details related to the VPC Block Public Access (BPA) options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcBlockPublicAccessOptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_block_public_access_options" in value:
        import capo_ec2.types.vpc_block_public_access_options

        capo_ec2.types.vpc_block_public_access_options.serialize_ec2_query(
            value["vpc_block_public_access_options"],
            pairs,
            f"{key_prefix}VpcBlockPublicAccessOptions",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcBlockPublicAccessOptionsResult:
    out: ModifyVpcBlockPublicAccessOptionsResult = {}  # type: ignore[typeddict-item]
    child_vpc_block_public_access_options = el.find("vpcBlockPublicAccessOptions")
    if child_vpc_block_public_access_options is not None:
        import capo_ec2.types.vpc_block_public_access_options

        out["vpc_block_public_access_options"] = (
            capo_ec2.types.vpc_block_public_access_options.deserialize_ec2_query(
                child_vpc_block_public_access_options
            )
        )
    return out
