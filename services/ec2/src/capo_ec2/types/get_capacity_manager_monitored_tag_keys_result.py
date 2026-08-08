"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMonitoredTagKeysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_monitored_tag_key_list
    import capo_ec2.types.string


class GetCapacityManagerMonitoredTagKeysResult(TypedDict, closed=True):
    capacity_manager_tag_keys: NotRequired[
        "capo_ec2.types.capacity_manager_monitored_tag_key_list.CapacityManagerMonitoredTagKeyList"
    ]
    """<p> The list of tag keys being monitored by Capacity Manager, including their current status and metadata. </p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMonitoredTagKeysResult,
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
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMonitoredTagKeysResult:
    out: GetCapacityManagerMonitoredTagKeysResult = {}  # type: ignore[typeddict-item]
    if el.find("capacityManagerTagKeySet") is not None:
        import capo_ec2.types.capacity_manager_monitored_tag_key_list

        out["capacity_manager_tag_keys"] = (
            capo_ec2.types.capacity_manager_monitored_tag_key_list.deserialize_ec2_query(
                el, "capacityManagerTagKeySet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
