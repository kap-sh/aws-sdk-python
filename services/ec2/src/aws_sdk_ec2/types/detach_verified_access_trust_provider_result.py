"""Generated from Smithy shape ``com.amazonaws.ec2#DetachVerifiedAccessTrustProviderResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance
    import aws_sdk_ec2.types.verified_access_trust_provider


class DetachVerifiedAccessTrustProviderResult(TypedDict):
    verified_access_trust_provider: NotRequired[
        "aws_sdk_ec2.types.verified_access_trust_provider.VerifiedAccessTrustProvider"
    ]
    """<p>Details about the Verified Access trust provider.</p>"""
    verified_access_instance: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance.VerifiedAccessInstance"
    ]
    """<p>Details about the Verified Access instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DetachVerifiedAccessTrustProviderResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_trust_provider" in value:
        import aws_sdk_ec2.types.verified_access_trust_provider

        aws_sdk_ec2.types.verified_access_trust_provider.serialize_ec2_query(
            value["verified_access_trust_provider"],
            pairs,
            f"{prefix}.VerifiedAccessTrustProvider",
        )
    if "verified_access_instance" in value:
        import aws_sdk_ec2.types.verified_access_instance

        aws_sdk_ec2.types.verified_access_instance.serialize_ec2_query(
            value["verified_access_instance"], pairs, f"{prefix}.VerifiedAccessInstance"
        )


def deserialize_ec2_query(el: Element) -> DetachVerifiedAccessTrustProviderResult:
    out: DetachVerifiedAccessTrustProviderResult = {}  # type: ignore[typeddict-item]
    child_verified_access_trust_provider = el.find("VerifiedAccessTrustProvider")
    if child_verified_access_trust_provider is not None:
        import aws_sdk_ec2.types.verified_access_trust_provider

        out["verified_access_trust_provider"] = (
            aws_sdk_ec2.types.verified_access_trust_provider.deserialize_ec2_query(
                child_verified_access_trust_provider
            )
        )
    child_verified_access_instance = el.find("VerifiedAccessInstance")
    if child_verified_access_instance is not None:
        import aws_sdk_ec2.types.verified_access_instance

        out["verified_access_instance"] = (
            aws_sdk_ec2.types.verified_access_instance.deserialize_ec2_query(
                child_verified_access_instance
            )
        )
    return out
