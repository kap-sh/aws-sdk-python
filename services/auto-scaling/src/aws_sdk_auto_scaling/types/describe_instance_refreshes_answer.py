"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeInstanceRefreshesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instance_refreshes
    import aws_sdk_auto_scaling.types.xml_string


class DescribeInstanceRefreshesAnswer(TypedDict, closed=True):
    instance_refreshes: NotRequired[
        "aws_sdk_auto_scaling.types.instance_refreshes.InstanceRefreshes"
    ]
    """<p>The instance refreshes for the specified group, sorted by creation timestamp in descending order.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInstanceRefreshesAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_refreshes" in value:
        import aws_sdk_auto_scaling.types.instance_refreshes

        aws_sdk_auto_scaling.types.instance_refreshes.serialize_query(
            value["instance_refreshes"], pairs, f"{prefix}.InstanceRefreshes"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeInstanceRefreshesAnswer:
    out: DescribeInstanceRefreshesAnswer = {}  # type: ignore[typeddict-item]
    child_instance_refreshes = el.find("InstanceRefreshes")
    if child_instance_refreshes is not None:
        import aws_sdk_auto_scaling.types.instance_refreshes

        out["instance_refreshes"] = (
            aws_sdk_auto_scaling.types.instance_refreshes.deserialize_query(
                child_instance_refreshes
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
