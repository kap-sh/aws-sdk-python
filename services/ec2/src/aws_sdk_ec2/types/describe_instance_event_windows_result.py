"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceEventWindowsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_set
    import aws_sdk_ec2.types.string


class DescribeInstanceEventWindowsResult(TypedDict):
    instance_event_windows: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_set.InstanceEventWindowSet"
    ]
    """<p>Information about the event windows.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceEventWindowsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_event_windows" in value:
        import aws_sdk_ec2.types.instance_event_window_set

        aws_sdk_ec2.types.instance_event_window_set.serialize_ec2_query(
            value["instance_event_windows"], pairs, f"{prefix}.InstanceEventWindowSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceEventWindowsResult:
    out: DescribeInstanceEventWindowsResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceEventWindowSet") is not None:
        import aws_sdk_ec2.types.instance_event_window_set

        out["instance_event_windows"] = (
            aws_sdk_ec2.types.instance_event_window_set.deserialize_ec2_query(
                el, "InstanceEventWindowSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
