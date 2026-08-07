"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteTrustStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_store_arn


class DeleteTrustStoreInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTrustStoreInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_store_arn" in value:
        pairs.append((f"{key_prefix}TrustStoreArn", str(value["trust_store_arn"])))


def deserialize_query(el: Element) -> DeleteTrustStoreInput:
    out: DeleteTrustStoreInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    return out
