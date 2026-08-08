"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamExternalResourceVerificationTokenResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_external_resource_verification_token


class CreateIpamExternalResourceVerificationTokenResult(TypedDict, closed=True):
    ipam_external_resource_verification_token: NotRequired[
        "capo_ec2.types.ipam_external_resource_verification_token.IpamExternalResourceVerificationToken"
    ]
    """<p>The verification token.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamExternalResourceVerificationTokenResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_external_resource_verification_token" in value:
        import capo_ec2.types.ipam_external_resource_verification_token

        capo_ec2.types.ipam_external_resource_verification_token.serialize_ec2_query(
            value["ipam_external_resource_verification_token"],
            pairs,
            f"{key_prefix}IpamExternalResourceVerificationToken",
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateIpamExternalResourceVerificationTokenResult:
    out: CreateIpamExternalResourceVerificationTokenResult = {}  # type: ignore[typeddict-item]
    child_ipam_external_resource_verification_token = el.find(
        "ipamExternalResourceVerificationToken"
    )
    if child_ipam_external_resource_verification_token is not None:
        import capo_ec2.types.ipam_external_resource_verification_token

        out["ipam_external_resource_verification_token"] = (
            capo_ec2.types.ipam_external_resource_verification_token.deserialize_ec2_query(
                child_ipam_external_resource_verification_token
            )
        )
    return out
