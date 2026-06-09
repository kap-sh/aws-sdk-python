"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamScopesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamScopesResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_scopes: NotRequired["aws_sdk_ec2.types.ipam_scope_set.IpamScopeSet"]
    """<p>The scopes you want information on.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamScopesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "ipam_scopes" in value:
        import aws_sdk_ec2.types.ipam_scope_set

        aws_sdk_ec2.types.ipam_scope_set.serialize_ec2_query(
            value["ipam_scopes"], pairs, f"{prefix}.IpamScopeSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamScopesResult:
    out: DescribeIpamScopesResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("IpamScopeSet") is not None:
        import aws_sdk_ec2.types.ipam_scope_set

        out["ipam_scopes"] = aws_sdk_ec2.types.ipam_scope_set.deserialize_ec2_query(
            el, "IpamScopeSet"
        )
    return out
