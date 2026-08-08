"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerMonitoredTagKeysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_monitored_tag_key_list


class UpdateCapacityManagerMonitoredTagKeysResult(TypedDict, closed=True):
    capacity_manager_tag_keys: NotRequired[
        "capo_ec2.types.capacity_manager_monitored_tag_key_list.CapacityManagerMonitoredTagKeyList"
    ]
    """<p> The list of tag keys affected by the update, including their current status and metadata. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateCapacityManagerMonitoredTagKeysResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_manager_tag_keys" in value:
        import capo_ec2.types.capacity_manager_monitored_tag_key_list

        capo_ec2.types.capacity_manager_monitored_tag_key_list.serialize_ec2_query(
            value["capacity_manager_tag_keys"],
            pairs,
            f"{key_prefix}CapacityManagerTagKeySet",
        )


def deserialize_ec2_query(el: Element) -> UpdateCapacityManagerMonitoredTagKeysResult:
    out: UpdateCapacityManagerMonitoredTagKeysResult = {}  # type: ignore[typeddict-item]
    if el.find("capacityManagerTagKeySet") is not None:
        import capo_ec2.types.capacity_manager_monitored_tag_key_list

        out["capacity_manager_tag_keys"] = (
            capo_ec2.types.capacity_manager_monitored_tag_key_list.deserialize_ec2_query(
                el, "capacityManagerTagKeySet"
            )
        )
    return out
