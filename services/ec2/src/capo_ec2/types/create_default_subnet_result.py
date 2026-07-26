"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDefaultSubnetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.subnet


class CreateDefaultSubnetResult(TypedDict, closed=True):
    subnet: NotRequired["capo_ec2.types.subnet.Subnet"]
    """<p>Information about the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDefaultSubnetResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet" in value:
        import capo_ec2.types.subnet

        capo_ec2.types.subnet.serialize_ec2_query(
            value["subnet"], pairs, f"{prefix}.Subnet"
        )


def deserialize_ec2_query(el: Element) -> CreateDefaultSubnetResult:
    out: CreateDefaultSubnetResult = {}  # type: ignore[typeddict-item]
    child_subnet = el.find("Subnet")
    if child_subnet is not None:
        import capo_ec2.types.subnet

        out["subnet"] = capo_ec2.types.subnet.deserialize_ec2_query(child_subnet)
    return out
