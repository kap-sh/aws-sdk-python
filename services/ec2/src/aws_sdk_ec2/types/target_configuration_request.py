"""Generated from Smithy shape ``com.amazonaws.ec2#TargetConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.reserved_instances_offering_id


class TargetConfigurationRequest(TypedDict, closed=True):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances the Convertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request</p>"""
    offering_id: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_offering_id.ReservedInstancesOfferingId"
    ]
    """<p>The Convertible Reserved Instance offering ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetConfigurationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "offering_id" in value:
        pairs.append((f"{prefix}.OfferingId", str(value["offering_id"])))


def deserialize_ec2_query(el: Element) -> TargetConfigurationRequest:
    out: TargetConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_offering_id = el.find("OfferingId")
    if child_offering_id is not None:
        out["offering_id"] = str(child_offering_id.text or "")
    return out
