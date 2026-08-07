"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoresInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.page_size
    import capo_elastic_load_balancing_v2.types.trust_store_arns
    import capo_elastic_load_balancing_v2.types.trust_store_names


class DescribeTrustStoresInput(TypedDict, closed=True):
    trust_store_arns: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arns.TrustStoreArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    names: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_names.TrustStoreNames"
    ]
    """<p>The names of the trust stores.</p>"""
    marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["capo_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoresInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_store_arns" in value:
        import capo_elastic_load_balancing_v2.types.trust_store_arns

        capo_elastic_load_balancing_v2.types.trust_store_arns.serialize_query(
            value["trust_store_arns"], pairs, f"{key_prefix}TrustStoreArns"
        )
    if "names" in value:
        import capo_elastic_load_balancing_v2.types.trust_store_names

        capo_elastic_load_balancing_v2.types.trust_store_names.serialize_query(
            value["names"], pairs, f"{key_prefix}Names"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{key_prefix}PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeTrustStoresInput:
    out: DescribeTrustStoresInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arns = el.find("TrustStoreArns")
    if child_trust_store_arns is not None:
        import capo_elastic_load_balancing_v2.types.trust_store_arns

        out["trust_store_arns"] = (
            capo_elastic_load_balancing_v2.types.trust_store_arns.deserialize_query(
                child_trust_store_arns
            )
        )
    child_names = el.find("Names")
    if child_names is not None:
        import capo_elastic_load_balancing_v2.types.trust_store_names

        out["names"] = (
            capo_elastic_load_balancing_v2.types.trust_store_names.deserialize_query(
                child_names
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
