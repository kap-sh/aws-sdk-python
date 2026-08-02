"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDefaultVpcResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc


class CreateDefaultVpcResult(TypedDict, closed=True):
    vpc: NotRequired["capo_ec2.types.vpc.Vpc"]
    """<p>Information about the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDefaultVpcResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc" in value:
        import capo_ec2.types.vpc

        capo_ec2.types.vpc.serialize_ec2_query(value["vpc"], pairs, f"{key_prefix}Vpc")


def deserialize_ec2_query(el: Element) -> CreateDefaultVpcResult:
    out: CreateDefaultVpcResult = {}  # type: ignore[typeddict-item]
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        import capo_ec2.types.vpc

        out["vpc"] = capo_ec2.types.vpc.deserialize_ec2_query(child_vpc)
    return out
