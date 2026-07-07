"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeInfoFromInstanceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceTypeInfoFromInstanceRequirements(TypedDict, closed=True):
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The matching instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeInfoFromInstanceRequirements,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))


def deserialize_ec2_query(el: Element) -> InstanceTypeInfoFromInstanceRequirements:
    out: InstanceTypeInfoFromInstanceRequirements = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    return out
