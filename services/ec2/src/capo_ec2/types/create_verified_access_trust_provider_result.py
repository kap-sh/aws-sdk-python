"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessTrustProviderResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_trust_provider


class CreateVerifiedAccessTrustProviderResult(TypedDict, closed=True):
    verified_access_trust_provider: NotRequired[
        "capo_ec2.types.verified_access_trust_provider.VerifiedAccessTrustProvider"
    ]
    """<p>Details about the Verified Access trust provider.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessTrustProviderResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_trust_provider" in value:
        import capo_ec2.types.verified_access_trust_provider

        capo_ec2.types.verified_access_trust_provider.serialize_ec2_query(
            value["verified_access_trust_provider"],
            pairs,
            f"{prefix}.VerifiedAccessTrustProvider",
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessTrustProviderResult:
    out: CreateVerifiedAccessTrustProviderResult = {}  # type: ignore[typeddict-item]
    child_verified_access_trust_provider = el.find("VerifiedAccessTrustProvider")
    if child_verified_access_trust_provider is not None:
        import capo_ec2.types.verified_access_trust_provider

        out["verified_access_trust_provider"] = (
            capo_ec2.types.verified_access_trust_provider.deserialize_ec2_query(
                child_verified_access_trust_provider
            )
        )
    return out
