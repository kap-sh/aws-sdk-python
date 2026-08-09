"""Generated from Smithy shape ``com.amazonaws.ec2#RunScheduledInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id_set


class RunScheduledInstancesResult(TypedDict, closed=True):
    instance_id_set: NotRequired["capo_ec2.types.instance_id_set.InstanceIdSet"]
    """<p>The IDs of the newly launched instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RunScheduledInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id_set" in value:
        import capo_ec2.types.instance_id_set

        capo_ec2.types.instance_id_set.serialize_ec2_query(
            value["instance_id_set"], pairs, f"{key_prefix}InstanceIdSet"
        )


def deserialize_ec2_query(el: Element) -> RunScheduledInstancesResult:
    out: RunScheduledInstancesResult = {}  # type: ignore[typeddict-item]
    child_instance_id_set = el.find("instanceIdSet")
    if child_instance_id_set is not None:
        import capo_ec2.types.instance_id_set

        out["instance_id_set"] = capo_ec2.types.instance_id_set.deserialize_ec2_query(
            child_instance_id_set
        )
    return out
