"""Generated from Smithy shape ``com.amazonaws.ec2#AvailableCapacity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.available_instance_capacity_list
    import aws_sdk_ec2.types.integer


class AvailableCapacity(TypedDict):
    available_instance_capacity: NotRequired[
        "aws_sdk_ec2.types.available_instance_capacity_list.AvailableInstanceCapacityList"
    ]
    """<p>The number of instances that can be launched onto the Dedicated Host depending on the host's available capacity. For Dedicated Hosts that support multiple instance types, this parameter represents the number of instances for each instance size that is supported on the host.</p>"""
    available_v_cpus: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of vCPUs available for launching instances onto the Dedicated Host.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailableCapacity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "available_instance_capacity" in value:
        import aws_sdk_ec2.types.available_instance_capacity_list

        aws_sdk_ec2.types.available_instance_capacity_list.serialize_ec2_query(
            value["available_instance_capacity"],
            pairs,
            f"{prefix}.AvailableInstanceCapacity",
        )
    if "available_v_cpus" in value:
        pairs.append((f"{prefix}.AvailableVCpus", str(value["available_v_cpus"])))


def deserialize_ec2_query(el: Element) -> AvailableCapacity:
    out: AvailableCapacity = {}  # type: ignore[typeddict-item]
    if el.find("AvailableInstanceCapacity") is not None:
        import aws_sdk_ec2.types.available_instance_capacity_list

        out["available_instance_capacity"] = (
            aws_sdk_ec2.types.available_instance_capacity_list.deserialize_ec2_query(
                el, "AvailableInstanceCapacity"
            )
        )
    child_available_v_cpus = el.find("AvailableVCpus")
    if child_available_v_cpus is not None:
        out["available_v_cpus"] = int(child_available_v_cpus.text or "")
    return out
