"""Generated from Smithy shape ``com.amazonaws.ec2#StartInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_state_change_list


class StartInstancesResult(TypedDict, closed=True):
    starting_instances: NotRequired[
        "capo_ec2.types.instance_state_change_list.InstanceStateChangeList"
    ]
    """<p>Information about the started instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "starting_instances" in value:
        import capo_ec2.types.instance_state_change_list

        capo_ec2.types.instance_state_change_list.serialize_ec2_query(
            value["starting_instances"], pairs, f"{prefix}.InstancesSet"
        )


def deserialize_ec2_query(el: Element) -> StartInstancesResult:
    out: StartInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstancesSet") is not None:
        import capo_ec2.types.instance_state_change_list

        out["starting_instances"] = (
            capo_ec2.types.instance_state_change_list.deserialize_ec2_query(
                el, "InstancesSet"
            )
        )
    return out
