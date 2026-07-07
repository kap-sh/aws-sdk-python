"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoreAssociationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.marker
    import aws_sdk_elastic_load_balancing_v2.types.page_size
    import aws_sdk_elastic_load_balancing_v2.types.trust_store_arn


class DescribeTrustStoreAssociationsInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["aws_sdk_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoreAssociationsInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "trust_store_arn" in value:
        pairs.append((f"{prefix}.TrustStoreArn", str(value["trust_store_arn"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeTrustStoreAssociationsInput:
    out: DescribeTrustStoreAssociationsInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
