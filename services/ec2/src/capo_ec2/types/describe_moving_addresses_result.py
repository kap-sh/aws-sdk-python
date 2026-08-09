"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMovingAddressesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.moving_address_status_set
    import capo_ec2.types.string


class DescribeMovingAddressesResult(TypedDict, closed=True):
    moving_address_statuses: NotRequired[
        "capo_ec2.types.moving_address_status_set.MovingAddressStatusSet"
    ]
    """<p>The status for each Elastic IP address.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMovingAddressesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "moving_address_statuses" in value:
        import capo_ec2.types.moving_address_status_set

        capo_ec2.types.moving_address_status_set.serialize_ec2_query(
            value["moving_address_statuses"],
            pairs,
            f"{key_prefix}MovingAddressStatusSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMovingAddressesResult:
    out: DescribeMovingAddressesResult = {}  # type: ignore[typeddict-item]
    child_moving_address_statuses = el.find("movingAddressStatusSet")
    if child_moving_address_statuses is not None:
        import capo_ec2.types.moving_address_status_set

        out["moving_address_statuses"] = (
            capo_ec2.types.moving_address_status_set.deserialize_ec2_query(
                child_moving_address_statuses
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
