"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicePermissionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allowed_principal_set
    import capo_ec2.types.string


class DescribeVpcEndpointServicePermissionsResult(TypedDict, closed=True):
    allowed_principals: NotRequired[
        "capo_ec2.types.allowed_principal_set.AllowedPrincipalSet"
    ]
    """<p>Information about the allowed principals.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServicePermissionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allowed_principals" in value:
        import capo_ec2.types.allowed_principal_set

        capo_ec2.types.allowed_principal_set.serialize_ec2_query(
            value["allowed_principals"], pairs, f"{key_prefix}AllowedPrincipals"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointServicePermissionsResult:
    out: DescribeVpcEndpointServicePermissionsResult = {}  # type: ignore[typeddict-item]
    if el.find("allowedPrincipals") is not None:
        import capo_ec2.types.allowed_principal_set

        out["allowed_principals"] = (
            capo_ec2.types.allowed_principal_set.deserialize_ec2_query(
                el, "allowedPrincipals"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
