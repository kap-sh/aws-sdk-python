"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicePermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_principal_set
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointServicePermissionsResult(TypedDict):
    allowed_principals: NotRequired[
        "aws_sdk_ec2.types.allowed_principal_set.AllowedPrincipalSet"
    ]
    """<p>Information about the allowed principals.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServicePermissionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "allowed_principals" in value:
        import aws_sdk_ec2.types.allowed_principal_set

        aws_sdk_ec2.types.allowed_principal_set.serialize_ec2_query(
            value["allowed_principals"], pairs, f"{prefix}.AllowedPrincipals"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointServicePermissionsResult:
    out: DescribeVpcEndpointServicePermissionsResult = {}  # type: ignore[typeddict-item]
    if el.find("AllowedPrincipals") is not None:
        import aws_sdk_ec2.types.allowed_principal_set

        out["allowed_principals"] = (
            aws_sdk_ec2.types.allowed_principal_set.deserialize_ec2_query(
                el, "AllowedPrincipals"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
