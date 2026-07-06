"""Generated from Smithy shape ``com.amazonaws.ec2#RunScheduledInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id_set


class RunScheduledInstancesResult(TypedDict, closed=True):
    instance_id_set: NotRequired["aws_sdk_ec2.types.instance_id_set.InstanceIdSet"]
    """<p>The IDs of the newly launched instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RunScheduledInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id_set" in value:
        import aws_sdk_ec2.types.instance_id_set

        aws_sdk_ec2.types.instance_id_set.serialize_ec2_query(
            value["instance_id_set"], pairs, f"{prefix}.InstanceIdSet"
        )


def deserialize_ec2_query(el: Element) -> RunScheduledInstancesResult:
    out: RunScheduledInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIdSet") is not None:
        import aws_sdk_ec2.types.instance_id_set

        out["instance_id_set"] = (
            aws_sdk_ec2.types.instance_id_set.deserialize_ec2_query(el, "InstanceIdSet")
        )
    return out
