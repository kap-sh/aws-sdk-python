"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoreRevocationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation

DescribeTrustStoreRevocationResponse: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation.DescribeTrustStoreRevocation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoreRevocationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DescribeTrustStoreRevocationResponse:
    import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation

    out: DescribeTrustStoreRevocationResponse = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: DescribeTrustStoreRevocationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> DescribeTrustStoreRevocationResponse:
    import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation

    out: DescribeTrustStoreRevocationResponse = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation.deserialize_query(
                child
            )
        )
    return out
