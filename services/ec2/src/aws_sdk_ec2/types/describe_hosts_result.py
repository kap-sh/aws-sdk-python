"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_list
    import aws_sdk_ec2.types.string


class DescribeHostsResult(TypedDict, closed=True):
    hosts: NotRequired["aws_sdk_ec2.types.host_list.HostList"]
    """<p>Information about the Dedicated Hosts.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeHostsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hosts" in value:
        import aws_sdk_ec2.types.host_list

        aws_sdk_ec2.types.host_list.serialize_ec2_query(
            value["hosts"], pairs, f"{prefix}.HostSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeHostsResult:
    out: DescribeHostsResult = {}  # type: ignore[typeddict-item]
    if el.find("HostSet") is not None:
        import aws_sdk_ec2.types.host_list

        out["hosts"] = aws_sdk_ec2.types.host_list.deserialize_ec2_query(el, "HostSet")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
