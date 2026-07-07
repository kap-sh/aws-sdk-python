"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddTrustStoreRevocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.trust_store_revocations


class AddTrustStoreRevocationsOutput(TypedDict, closed=True):
    trust_store_revocations: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_store_revocations.TrustStoreRevocations"
    ]
    """<p>Information about the revocation file added to the trust store.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTrustStoreRevocationsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_store_revocations" in value:
        import aws_sdk_elastic_load_balancing_v2.types.trust_store_revocations

        aws_sdk_elastic_load_balancing_v2.types.trust_store_revocations.serialize_query(
            value["trust_store_revocations"], pairs, f"{prefix}.TrustStoreRevocations"
        )


def deserialize_query(el: Element) -> AddTrustStoreRevocationsOutput:
    out: AddTrustStoreRevocationsOutput = {}  # type: ignore[typeddict-item]
    child_trust_store_revocations = el.find("TrustStoreRevocations")
    if child_trust_store_revocations is not None:
        import aws_sdk_elastic_load_balancing_v2.types.trust_store_revocations

        out["trust_store_revocations"] = (
            aws_sdk_elastic_load_balancing_v2.types.trust_store_revocations.deserialize_query(
                child_trust_store_revocations
            )
        )
    return out
