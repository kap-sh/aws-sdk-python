"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoreRevocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.page_size
    import capo_elastic_load_balancing_v2.types.revocation_ids
    import capo_elastic_load_balancing_v2.types.trust_store_arn


class DescribeTrustStoreRevocationsInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    revocation_ids: NotRequired[
        "capo_elastic_load_balancing_v2.types.revocation_ids.RevocationIds"
    ]
    """<p>The revocation IDs of the revocation files you want to describe.</p>"""
    marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["capo_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoreRevocationsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_store_arn" in value:
        pairs.append((f"{key_prefix}TrustStoreArn", str(value["trust_store_arn"])))
    if "revocation_ids" in value:
        import capo_elastic_load_balancing_v2.types.revocation_ids

        capo_elastic_load_balancing_v2.types.revocation_ids.serialize_query(
            value["revocation_ids"], pairs, f"{key_prefix}RevocationIds"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{key_prefix}PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeTrustStoreRevocationsInput:
    out: DescribeTrustStoreRevocationsInput = {}  # type: ignore[typeddict-item]
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
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
