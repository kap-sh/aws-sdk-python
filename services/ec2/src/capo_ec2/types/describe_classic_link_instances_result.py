"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClassicLinkInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.classic_link_instance_list
    import capo_ec2.types.string


class DescribeClassicLinkInstancesResult(TypedDict, closed=True):
    instances: NotRequired[
        "capo_ec2.types.classic_link_instance_list.ClassicLinkInstanceList"
    ]
    """<p>Information about one or more linked EC2-Classic instances.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClassicLinkInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instances" in value:
        import capo_ec2.types.classic_link_instance_list

        capo_ec2.types.classic_link_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}InstancesSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClassicLinkInstancesResult:
    out: DescribeClassicLinkInstancesResult = {}  # type: ignore[typeddict-item]
    child_instances = el.find("instancesSet")
    if child_instances is not None:
        import capo_ec2.types.classic_link_instance_list

        out["instances"] = (
            capo_ec2.types.classic_link_instance_list.deserialize_ec2_query(
                child_instances
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
