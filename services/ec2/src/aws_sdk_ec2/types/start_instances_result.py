"""Generated from Smithy shape ``com.amazonaws.ec2#StartInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state_change_list


class StartInstancesResult(TypedDict):
    starting_instances: NotRequired[
        "aws_sdk_ec2.types.instance_state_change_list.InstanceStateChangeList"
    ]
    """<p>Information about the started instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "starting_instances" in value:
        import aws_sdk_ec2.types.instance_state_change_list

        aws_sdk_ec2.types.instance_state_change_list.serialize_ec2_query(
            value["starting_instances"], pairs, f"{prefix}.InstancesSet"
        )


def deserialize_ec2_query(el: Element) -> StartInstancesResult:
    out: StartInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstancesSet") is not None:
        import aws_sdk_ec2.types.instance_state_change_list

        out["starting_instances"] = (
            aws_sdk_ec2.types.instance_state_change_list.deserialize_ec2_query(
                el, "InstancesSet"
            )
        )
    return out
