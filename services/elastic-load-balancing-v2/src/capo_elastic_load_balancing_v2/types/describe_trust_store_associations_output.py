"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoreAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.trust_store_associations


class DescribeTrustStoreAssociationsOutput(TypedDict, closed=True):
    trust_store_associations: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_associations.TrustStoreAssociations"
    ]
    """<p>Information about the resources the trust store is associated to.</p>"""
    next_marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoreAssociationsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_store_associations" in value:
        import capo_elastic_load_balancing_v2.types.trust_store_associations

        capo_elastic_load_balancing_v2.types.trust_store_associations.serialize_query(
            value["trust_store_associations"],
            pairs,
            f"{key_prefix}TrustStoreAssociations",
        )
    if "next_marker" in value:
        pairs.append((f"{key_prefix}NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeTrustStoreAssociationsOutput:
    out: DescribeTrustStoreAssociationsOutput = {}  # type: ignore[typeddict-item]
    child_trust_store_associations = el.find("TrustStoreAssociations")
    if child_trust_store_associations is not None:
        import capo_elastic_load_balancing_v2.types.trust_store_associations

        out["trust_store_associations"] = (
            capo_elastic_load_balancing_v2.types.trust_store_associations.deserialize_query(
                child_trust_store_associations
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
