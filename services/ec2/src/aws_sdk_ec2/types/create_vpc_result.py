"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc


class CreateVpcResult(TypedDict):
    vpc: NotRequired["aws_sdk_ec2.types.vpc.Vpc"]
    """<p>Information about the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc" in value:
        import aws_sdk_ec2.types.vpc

        aws_sdk_ec2.types.vpc.serialize_ec2_query(value["vpc"], pairs, f"{prefix}.Vpc")


def deserialize_ec2_query(el: Element) -> CreateVpcResult:
    out: CreateVpcResult = {}  # type: ignore[typeddict-item]
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        import aws_sdk_ec2.types.vpc

        out["vpc"] = aws_sdk_ec2.types.vpc.deserialize_ec2_query(child_vpc)
    return out
