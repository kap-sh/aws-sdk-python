"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessEndpointTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_endpoint_target_list


class GetVerifiedAccessEndpointTargetsResult(TypedDict):
    verified_access_endpoint_targets: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_target_list.VerifiedAccessEndpointTargetList"
    ]
    """<p>The Verified Access targets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVerifiedAccessEndpointTargetsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_endpoint_targets" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_target_list

        aws_sdk_ec2.types.verified_access_endpoint_target_list.serialize_ec2_query(
            value["verified_access_endpoint_targets"],
            pairs,
            f"{prefix}.VerifiedAccessEndpointTargetSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetVerifiedAccessEndpointTargetsResult:
    out: GetVerifiedAccessEndpointTargetsResult = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessEndpointTargetSet") is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_target_list

        out["verified_access_endpoint_targets"] = (
            aws_sdk_ec2.types.verified_access_endpoint_target_list.deserialize_ec2_query(
                el, "VerifiedAccessEndpointTargetSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
