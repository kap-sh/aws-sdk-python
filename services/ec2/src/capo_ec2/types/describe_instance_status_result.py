"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_status_list
    import capo_ec2.types.string


class DescribeInstanceStatusResult(TypedDict, closed=True):
    instance_statuses: NotRequired[
        "capo_ec2.types.instance_status_list.InstanceStatusList"
    ]
    """<p>Information about the status of the instances.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_statuses" in value:
        import capo_ec2.types.instance_status_list

        capo_ec2.types.instance_status_list.serialize_ec2_query(
            value["instance_statuses"], pairs, f"{key_prefix}InstanceStatusSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceStatusResult:
    out: DescribeInstanceStatusResult = {}  # type: ignore[typeddict-item]
    child_instance_statuses = el.find("instanceStatusSet")
    if child_instance_statuses is not None:
        import capo_ec2.types.instance_status_list

        out["instance_statuses"] = (
            capo_ec2.types.instance_status_list.deserialize_ec2_query(
                child_instance_statuses
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
