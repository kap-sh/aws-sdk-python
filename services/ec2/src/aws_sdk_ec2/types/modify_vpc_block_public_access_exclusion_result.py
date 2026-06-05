"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcBlockPublicAccessExclusionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion


class ModifyVpcBlockPublicAccessExclusionResult(TypedDict):
    vpc_block_public_access_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion.VpcBlockPublicAccessExclusion"
    ]
    """<p>Details related to the exclusion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcBlockPublicAccessExclusionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_block_public_access_exclusion" in value:
        import aws_sdk_ec2.types.vpc_block_public_access_exclusion

        aws_sdk_ec2.types.vpc_block_public_access_exclusion.serialize_ec2_query(
            value["vpc_block_public_access_exclusion"],
            pairs,
            f"{prefix}.VpcBlockPublicAccessExclusion",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcBlockPublicAccessExclusionResult:
    out: ModifyVpcBlockPublicAccessExclusionResult = {}  # type: ignore[typeddict-item]
    child_vpc_block_public_access_exclusion = el.find("VpcBlockPublicAccessExclusion")
    if child_vpc_block_public_access_exclusion is not None:
        import aws_sdk_ec2.types.vpc_block_public_access_exclusion

        out["vpc_block_public_access_exclusion"] = (
            aws_sdk_ec2.types.vpc_block_public_access_exclusion.deserialize_ec2_query(
                child_vpc_block_public_access_exclusion
            )
        )
    return out
