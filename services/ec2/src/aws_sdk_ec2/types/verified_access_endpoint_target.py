"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_id


class VerifiedAccessEndpointTarget(TypedDict, closed=True):
    verified_access_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_id.VerifiedAccessEndpointId"
    ]
    """<p>The ID of the Verified Access endpoint.</p>"""
    verified_access_endpoint_target_ip_address: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The IP address of the target.</p>"""
    verified_access_endpoint_target_dns: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name of the target.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpointTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_endpoint_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessEndpointId",
                str(value["verified_access_endpoint_id"]),
            )
        )
    if "verified_access_endpoint_target_ip_address" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessEndpointTargetIpAddress",
                str(value["verified_access_endpoint_target_ip_address"]),
            )
        )
    if "verified_access_endpoint_target_dns" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessEndpointTargetDns",
                str(value["verified_access_endpoint_target_dns"]),
            )
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointTarget:
    out: VerifiedAccessEndpointTarget = {}  # type: ignore[typeddict-item]
    child_verified_access_endpoint_id = el.find("VerifiedAccessEndpointId")
    if child_verified_access_endpoint_id is not None:
        out["verified_access_endpoint_id"] = str(
            child_verified_access_endpoint_id.text or ""
        )
    child_verified_access_endpoint_target_ip_address = el.find(
        "VerifiedAccessEndpointTargetIpAddress"
    )
    if child_verified_access_endpoint_target_ip_address is not None:
        out["verified_access_endpoint_target_ip_address"] = str(
            child_verified_access_endpoint_target_ip_address.text or ""
        )
    child_verified_access_endpoint_target_dns = el.find(
        "VerifiedAccessEndpointTargetDns"
    )
    if child_verified_access_endpoint_target_dns is not None:
        out["verified_access_endpoint_target_dns"] = str(
            child_verified_access_endpoint_target_dns.text or ""
        )
    return out
