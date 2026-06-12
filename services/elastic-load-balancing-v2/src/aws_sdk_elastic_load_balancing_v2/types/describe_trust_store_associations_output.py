"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoreAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.trust_store_associations


class DescribeTrustStoreAssociationsOutput(TypedDict):
    trust_store_associations: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_store_associations.TrustStoreAssociations"
    ]
    """<p>Information about the resources the trust store is associated to.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoreAssociationsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "trust_store_associations" in value:
        import aws_sdk_elastic_load_balancing_v2.types.trust_store_associations

        aws_sdk_elastic_load_balancing_v2.types.trust_store_associations.serialize_query(
            value["trust_store_associations"], pairs, f"{prefix}.TrustStoreAssociations"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeTrustStoreAssociationsOutput:
    out: DescribeTrustStoreAssociationsOutput = {}  # type: ignore[typeddict-item]
    child_trust_store_associations = el.find("TrustStoreAssociations")
    if child_trust_store_associations is not None:
        import aws_sdk_elastic_load_balancing_v2.types.trust_store_associations

        out["trust_store_associations"] = (
            aws_sdk_elastic_load_balancing_v2.types.trust_store_associations.deserialize_query(
                child_trust_store_associations
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
