"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcBlockPublicAccessExclusionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_block_public_access_exclusion


class DeleteVpcBlockPublicAccessExclusionResult(TypedDict, closed=True):
    vpc_block_public_access_exclusion: NotRequired[
        "capo_ec2.types.vpc_block_public_access_exclusion.VpcBlockPublicAccessExclusion"
    ]
    """<p>Details about an exclusion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVpcBlockPublicAccessExclusionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_block_public_access_exclusion" in value:
        import capo_ec2.types.vpc_block_public_access_exclusion

        capo_ec2.types.vpc_block_public_access_exclusion.serialize_ec2_query(
            value["vpc_block_public_access_exclusion"],
            pairs,
            f"{prefix}.VpcBlockPublicAccessExclusion",
        )


def deserialize_ec2_query(el: Element) -> DeleteVpcBlockPublicAccessExclusionResult:
    out: DeleteVpcBlockPublicAccessExclusionResult = {}  # type: ignore[typeddict-item]
    child_vpc_block_public_access_exclusion = el.find("VpcBlockPublicAccessExclusion")
    if child_vpc_block_public_access_exclusion is not None:
        import capo_ec2.types.vpc_block_public_access_exclusion

        out["vpc_block_public_access_exclusion"] = (
            capo_ec2.types.vpc_block_public_access_exclusion.deserialize_ec2_query(
                child_vpc_block_public_access_exclusion
            )
        )
    return out
