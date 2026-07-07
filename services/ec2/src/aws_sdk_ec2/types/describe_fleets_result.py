"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_set
    import aws_sdk_ec2.types.string


class DescribeFleetsResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    fleets: NotRequired["aws_sdk_ec2.types.fleet_set.FleetSet"]
    """<p>Information about the EC2 Fleets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "fleets" in value:
        import aws_sdk_ec2.types.fleet_set

        aws_sdk_ec2.types.fleet_set.serialize_ec2_query(
            value["fleets"], pairs, f"{prefix}.FleetSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeFleetsResult:
    out: DescribeFleetsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("FleetSet") is not None:
        import aws_sdk_ec2.types.fleet_set

        out["fleets"] = aws_sdk_ec2.types.fleet_set.deserialize_ec2_query(
            el, "FleetSet"
        )
    return out
