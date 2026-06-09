"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMonitoredTagKeysResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list
    import aws_sdk_ec2.types.string


class GetCapacityManagerMonitoredTagKeysResult(TypedDict):
    capacity_manager_tag_keys: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.CapacityManagerMonitoredTagKeyList"
    ]
    """<p> The list of tag keys being monitored by Capacity Manager, including their current status and metadata. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMonitoredTagKeysResult,
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
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMonitoredTagKeysResult:
    out: GetCapacityManagerMonitoredTagKeysResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityManagerTagKeySet") is not None:
        import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list

        out["capacity_manager_tag_keys"] = (
            aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.deserialize_ec2_query(
                el, "CapacityManagerTagKeySet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
