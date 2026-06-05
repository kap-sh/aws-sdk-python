"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeStaleSecurityGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stale_security_group_set
    import aws_sdk_ec2.types.string


class DescribeStaleSecurityGroupsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    stale_security_group_set: NotRequired[
        "aws_sdk_ec2.types.stale_security_group_set.StaleSecurityGroupSet"
    ]
    """<p>Information about the stale security groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeStaleSecurityGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "stale_security_group_set" in value:
        import aws_sdk_ec2.types.stale_security_group_set

        aws_sdk_ec2.types.stale_security_group_set.serialize_ec2_query(
            value["stale_security_group_set"], pairs, f"{prefix}.StaleSecurityGroupSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeStaleSecurityGroupsResult:
    out: DescribeStaleSecurityGroupsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("StaleSecurityGroupSet") is not None:
        import aws_sdk_ec2.types.stale_security_group_set

        out["stale_security_group_set"] = (
            aws_sdk_ec2.types.stale_security_group_set.deserialize_ec2_query(
                el, "StaleSecurityGroupSet"
            )
        )
    return out
