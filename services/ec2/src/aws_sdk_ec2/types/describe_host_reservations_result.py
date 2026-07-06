"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_reservation_set
    import aws_sdk_ec2.types.string


class DescribeHostReservationsResult(TypedDict, closed=True):
    host_reservation_set: NotRequired[
        "aws_sdk_ec2.types.host_reservation_set.HostReservationSet"
    ]
    """<p>Details about the reservation's configuration.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeHostReservationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "host_reservation_set" in value:
        import aws_sdk_ec2.types.host_reservation_set

        aws_sdk_ec2.types.host_reservation_set.serialize_ec2_query(
            value["host_reservation_set"], pairs, f"{prefix}.HostReservationSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeHostReservationsResult:
    out: DescribeHostReservationsResult = {}  # type: ignore[typeddict-item]
    if el.find("HostReservationSet") is not None:
        import aws_sdk_ec2.types.host_reservation_set

        out["host_reservation_set"] = (
            aws_sdk_ec2.types.host_reservation_set.deserialize_ec2_query(
                el, "HostReservationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
