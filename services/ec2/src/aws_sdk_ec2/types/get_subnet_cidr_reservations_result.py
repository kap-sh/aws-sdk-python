"""Generated from Smithy shape ``com.amazonaws.ec2#GetSubnetCidrReservationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_reservation_list


class GetSubnetCidrReservationsResult(TypedDict):
    subnet_ipv4_cidr_reservations: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_list.SubnetCidrReservationList"
    ]
    """<p>Information about the IPv4 subnet CIDR reservations.</p>"""
    subnet_ipv6_cidr_reservations: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_list.SubnetCidrReservationList"
    ]
    """<p>Information about the IPv6 subnet CIDR reservations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetSubnetCidrReservationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_ipv4_cidr_reservations" in value:
        import aws_sdk_ec2.types.subnet_cidr_reservation_list

        aws_sdk_ec2.types.subnet_cidr_reservation_list.serialize_ec2_query(
            value["subnet_ipv4_cidr_reservations"],
            pairs,
            f"{prefix}.SubnetIpv4CidrReservationSet",
        )
    if "subnet_ipv6_cidr_reservations" in value:
        import aws_sdk_ec2.types.subnet_cidr_reservation_list

        aws_sdk_ec2.types.subnet_cidr_reservation_list.serialize_ec2_query(
            value["subnet_ipv6_cidr_reservations"],
            pairs,
            f"{prefix}.SubnetIpv6CidrReservationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetSubnetCidrReservationsResult:
    out: GetSubnetCidrReservationsResult = {}  # type: ignore[typeddict-item]
    if el.find("SubnetIpv4CidrReservationSet") is not None:
        import aws_sdk_ec2.types.subnet_cidr_reservation_list

        out["subnet_ipv4_cidr_reservations"] = (
            aws_sdk_ec2.types.subnet_cidr_reservation_list.deserialize_ec2_query(
                el, "SubnetIpv4CidrReservationSet"
            )
        )
    if el.find("SubnetIpv6CidrReservationSet") is not None:
        import aws_sdk_ec2.types.subnet_cidr_reservation_list

        out["subnet_ipv6_cidr_reservations"] = (
            aws_sdk_ec2.types.subnet_cidr_reservation_list.deserialize_ec2_query(
                el, "SubnetIpv6CidrReservationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
