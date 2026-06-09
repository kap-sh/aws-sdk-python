"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceStatusResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_list
    import aws_sdk_ec2.types.string


class DescribeInstanceStatusResult(TypedDict):
    instance_statuses: NotRequired[
        "aws_sdk_ec2.types.instance_status_list.InstanceStatusList"
    ]
    """<p>Information about the status of the instances.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_statuses" in value:
        import aws_sdk_ec2.types.instance_status_list

        aws_sdk_ec2.types.instance_status_list.serialize_ec2_query(
            value["instance_statuses"], pairs, f"{prefix}.InstanceStatusSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceStatusResult:
    out: DescribeInstanceStatusResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceStatusSet") is not None:
        import aws_sdk_ec2.types.instance_status_list

        out["instance_statuses"] = (
            aws_sdk_ec2.types.instance_status_list.deserialize_ec2_query(
                el, "InstanceStatusSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
