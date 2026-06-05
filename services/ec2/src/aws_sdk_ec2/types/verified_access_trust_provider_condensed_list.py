"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProviderCondensedList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_trust_provider_condensed

VerifiedAccessTrustProviderCondensedList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_trust_provider_condensed.VerifiedAccessTrustProviderCondensed"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessTrustProviderCondensedList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.verified_access_trust_provider_condensed

        aws_sdk_ec2.types.verified_access_trust_provider_condensed.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VerifiedAccessTrustProviderCondensedList:
    import aws_sdk_ec2.types.verified_access_trust_provider_condensed

    out: VerifiedAccessTrustProviderCondensedList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.verified_access_trust_provider_condensed.deserialize_ec2_query(
                child
            )
        )
    return out
