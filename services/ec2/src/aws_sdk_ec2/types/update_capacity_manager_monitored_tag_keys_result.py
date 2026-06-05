"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerMonitoredTagKeysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list


class UpdateCapacityManagerMonitoredTagKeysResult(TypedDict):
    capacity_manager_tag_keys: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.CapacityManagerMonitoredTagKeyList"
    ]
    """<p> The list of tag keys affected by the update, including their current status and metadata. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateCapacityManagerMonitoredTagKeysResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_manager_tag_keys" in value:
        import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list

        aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.serialize_ec2_query(
            value["capacity_manager_tag_keys"],
            pairs,
            f"{prefix}.CapacityManagerTagKeySet",
        )


def deserialize_ec2_query(el: Element) -> UpdateCapacityManagerMonitoredTagKeysResult:
    out: UpdateCapacityManagerMonitoredTagKeysResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityManagerTagKeySet") is not None:
        import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list

        out["capacity_manager_tag_keys"] = (
            aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.deserialize_ec2_query(
                el, "CapacityManagerTagKeySet"
            )
        )
    return out
