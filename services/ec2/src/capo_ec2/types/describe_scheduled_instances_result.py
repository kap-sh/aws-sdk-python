"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instance_set
    import capo_ec2.types.string


class DescribeScheduledInstancesResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token required to retrieve the next set of results. This value is <code>null</code> when there are no more results to return.</p>"""
    scheduled_instance_set: NotRequired[
        "capo_ec2.types.scheduled_instance_set.ScheduledInstanceSet"
    ]
    """<p>Information about the Scheduled Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeScheduledInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "scheduled_instance_set" in value:
        import capo_ec2.types.scheduled_instance_set

        capo_ec2.types.scheduled_instance_set.serialize_ec2_query(
            value["scheduled_instance_set"], pairs, f"{key_prefix}ScheduledInstanceSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeScheduledInstancesResult:
    out: DescribeScheduledInstancesResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("scheduledInstanceSet") is not None:
        import capo_ec2.types.scheduled_instance_set

        out["scheduled_instance_set"] = (
            capo_ec2.types.scheduled_instance_set.deserialize_ec2_query(
                el, "scheduledInstanceSet"
            )
        )
    return out
