"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state_change_list


class TerminateInstancesResult(TypedDict):
    terminating_instances: NotRequired[
        "aws_sdk_ec2.types.instance_state_change_list.InstanceStateChangeList"
    ]
    """<p>Information about the terminated instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "terminating_instances" in value:
        import aws_sdk_ec2.types.instance_state_change_list

        aws_sdk_ec2.types.instance_state_change_list.serialize_ec2_query(
            value["terminating_instances"], pairs, f"{prefix}.InstancesSet"
        )


def deserialize_ec2_query(el: Element) -> TerminateInstancesResult:
    out: TerminateInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstancesSet") is not None:
        import aws_sdk_ec2.types.instance_state_change_list

        out["terminating_instances"] = (
            aws_sdk_ec2.types.instance_state_change_list.deserialize_ec2_query(
                el, "InstancesSet"
            )
        )
    return out
