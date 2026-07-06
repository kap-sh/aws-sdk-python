"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTrustStoreRevocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation_response
    import aws_sdk_elastic_load_balancing_v2.types.marker


class DescribeTrustStoreRevocationsOutput(TypedDict, closed=True):
    trust_store_revocations: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation_response.DescribeTrustStoreRevocationResponse"
    ]
    """<p>Information about the revocation file in the trust store.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrustStoreRevocationsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "trust_store_revocations" in value:
        import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation_response

        aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation_response.serialize_query(
            value["trust_store_revocations"], pairs, f"{prefix}.TrustStoreRevocations"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeTrustStoreRevocationsOutput:
    out: DescribeTrustStoreRevocationsOutput = {}  # type: ignore[typeddict-item]
    child_trust_store_revocations = el.find("TrustStoreRevocations")
    if child_trust_store_revocations is not None:
        import aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation_response

        out["trust_store_revocations"] = (
            aws_sdk_elastic_load_balancing_v2.types.describe_trust_store_revocation_response.deserialize_query(
                child_trust_store_revocations
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
