"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveTrustStoreRevocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.revocation_ids
    import capo_elastic_load_balancing_v2.types.trust_store_arn


class RemoveTrustStoreRevocationsInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    revocation_ids: NotRequired[
        "capo_elastic_load_balancing_v2.types.revocation_ids.RevocationIds"
    ]
    """<p>The revocation IDs of the revocation files you want to remove.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTrustStoreRevocationsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_store_arn" in value:
        pairs.append((f"{prefix}.TrustStoreArn", str(value["trust_store_arn"])))
    if "revocation_ids" in value:
        import capo_elastic_load_balancing_v2.types.revocation_ids

        capo_elastic_load_balancing_v2.types.revocation_ids.serialize_query(
            value["revocation_ids"], pairs, f"{prefix}.RevocationIds"
        )


def deserialize_query(el: Element) -> RemoveTrustStoreRevocationsInput:
    out: RemoveTrustStoreRevocationsInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_revocation_ids = el.find("RevocationIds")
    if child_revocation_ids is not None:
        import capo_elastic_load_balancing_v2.types.revocation_ids

        out["revocation_ids"] = (
            capo_elastic_load_balancing_v2.types.revocation_ids.deserialize_query(
                child_revocation_ids
            )
        )
    return out
