"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstanceAvailabilityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instance_availability_set
    import aws_sdk_ec2.types.string


class DescribeScheduledInstanceAvailabilityResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token required to retrieve the next set of results. This value is <code>null</code> when there are no more results to return.</p>"""
    scheduled_instance_availability_set: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_availability_set.ScheduledInstanceAvailabilitySet"
    ]
    """<p>Information about the available Scheduled Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeScheduledInstanceAvailabilityResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "scheduled_instance_availability_set" in value:
        import aws_sdk_ec2.types.scheduled_instance_availability_set

        aws_sdk_ec2.types.scheduled_instance_availability_set.serialize_ec2_query(
            value["scheduled_instance_availability_set"],
            pairs,
            f"{prefix}.ScheduledInstanceAvailabilitySet",
        )


def deserialize_ec2_query(el: Element) -> DescribeScheduledInstanceAvailabilityResult:
    out: DescribeScheduledInstanceAvailabilityResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ScheduledInstanceAvailabilitySet") is not None:
        import aws_sdk_ec2.types.scheduled_instance_availability_set

        out["scheduled_instance_availability_set"] = (
            aws_sdk_ec2.types.scheduled_instance_availability_set.deserialize_ec2_query(
                el, "ScheduledInstanceAvailabilitySet"
            )
        )
    return out
