"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointPayerResponsibilityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.payer_responsibility_set
    import capo_ec2.types.string


class ModifyVpcEndpointPayerResponsibilityResult(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint.</p>"""
    payer_responsibilities: NotRequired[
        "capo_ec2.types.payer_responsibility_set.PayerResponsibilitySet"
    ]
    """<p>The payer responsibility settings for the VPC endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointPayerResponsibilityResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "payer_responsibilities" in value:
        import capo_ec2.types.payer_responsibility_set

        capo_ec2.types.payer_responsibility_set.serialize_ec2_query(
            value["payer_responsibilities"],
            pairs,
            f"{key_prefix}PayerResponsibilitySet",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointPayerResponsibilityResult:
    out: ModifyVpcEndpointPayerResponsibilityResult = {}  # type: ignore[typeddict-item]
    child_vpc_endpoint_id = el.find("vpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_payer_responsibilities = el.find("payerResponsibilitySet")
    if child_payer_responsibilities is not None:
        import capo_ec2.types.payer_responsibility_set

        out["payer_responsibilities"] = (
            capo_ec2.types.payer_responsibility_set.deserialize_ec2_query(
                child_payer_responsibilities
            )
        )
    return out
