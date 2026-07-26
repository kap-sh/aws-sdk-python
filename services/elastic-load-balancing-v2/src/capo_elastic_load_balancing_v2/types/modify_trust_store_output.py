"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyTrustStoreOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.trust_stores


class ModifyTrustStoreOutput(TypedDict, closed=True):
    trust_stores: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_stores.TrustStores"
    ]
    """<p>Information about the modified trust store.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTrustStoreOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_stores" in value:
        import capo_elastic_load_balancing_v2.types.trust_stores

        capo_elastic_load_balancing_v2.types.trust_stores.serialize_query(
            value["trust_stores"], pairs, f"{prefix}.TrustStores"
        )


def deserialize_query(el: Element) -> ModifyTrustStoreOutput:
    out: ModifyTrustStoreOutput = {}  # type: ignore[typeddict-item]
    child_trust_stores = el.find("TrustStores")
    if child_trust_stores is not None:
        import capo_elastic_load_balancing_v2.types.trust_stores

        out["trust_stores"] = (
            capo_elastic_load_balancing_v2.types.trust_stores.deserialize_query(
                child_trust_stores
            )
        )
    return out
