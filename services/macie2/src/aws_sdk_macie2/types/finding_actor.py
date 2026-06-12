"""Generated from Smithy shape ``com.amazonaws.macie2#FindingActor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.domain_details
    import aws_sdk_macie2.types.ip_address_details
    import aws_sdk_macie2.types.user_identity


class FindingActor(TypedDict):
    domain_details: NotRequired["aws_sdk_macie2.types.domain_details.DomainDetails"]
    """<p>The domain name of the device that the entity used to perform the action on the affected resource.</p>"""
    ip_address_details: NotRequired[
        "aws_sdk_macie2.types.ip_address_details.IpAddressDetails"
    ]
    """<p>The IP address and related details about the device that the entity used to perform the action on the affected resource. The details can include information such as the owner and geographic location of the IP address.</p>"""
    user_identity: NotRequired["aws_sdk_macie2.types.user_identity.UserIdentity"]
    """<p>The type and other characteristics of the entity that performed the action on the affected resource. This value is null if the action was performed by an anonymous (unauthenticated) entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingActor) -> dict:
    out: dict = {}
    if "domain_details" in value:
        import aws_sdk_macie2.types.domain_details

        out["domainDetails"] = aws_sdk_macie2.types.domain_details.serialize_json(
            value["domain_details"]
        )
    if "ip_address_details" in value:
        import aws_sdk_macie2.types.ip_address_details

        out["ipAddressDetails"] = (
            aws_sdk_macie2.types.ip_address_details.serialize_json(
                value["ip_address_details"]
            )
        )
    if "user_identity" in value:
        import aws_sdk_macie2.types.user_identity

        out["userIdentity"] = aws_sdk_macie2.types.user_identity.serialize_json(
            value["user_identity"]
        )
    return out


def deserialize_json(data: dict) -> FindingActor:
    out: FindingActor = {}  # type: ignore[typeddict-item]
    if "domainDetails" in data:
        import aws_sdk_macie2.types.domain_details

        out["domain_details"] = aws_sdk_macie2.types.domain_details.deserialize_json(
            data["domainDetails"]
        )
    if "ipAddressDetails" in data:
        import aws_sdk_macie2.types.ip_address_details

        out["ip_address_details"] = (
            aws_sdk_macie2.types.ip_address_details.deserialize_json(
                data["ipAddressDetails"]
            )
        )
    if "userIdentity" in data:
        import aws_sdk_macie2.types.user_identity

        out["user_identity"] = aws_sdk_macie2.types.user_identity.deserialize_json(
            data["userIdentity"]
        )
    return out
