"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoresOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.trust_stores


class DescribeTrustStoresOutput(TypedDict, closed=True):
    trust_stores: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_stores.TrustStores"
    ]
    """<p>Information about the trust stores.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoresOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_stores" in value:
        import aws_sdk_elastic_load_balancing_v2.types.trust_stores

        aws_sdk_elastic_load_balancing_v2.types.trust_stores.serialize_query(
            value["trust_stores"], pairs, f"{prefix}.TrustStores"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeTrustStoresOutput:
    out: DescribeTrustStoresOutput = {}  # type: ignore[typeddict-item]
    child_trust_stores = el.find("TrustStores")
    if child_trust_stores is not None:
        import aws_sdk_elastic_load_balancing_v2.types.trust_stores

        out["trust_stores"] = (
            aws_sdk_elastic_load_balancing_v2.types.trust_stores.deserialize_query(
                child_trust_stores
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
