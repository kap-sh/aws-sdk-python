"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateTrustStoreOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.trust_stores


class CreateTrustStoreOutput(TypedDict):
    trust_stores: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_stores.TrustStores"
    ]
    """<p>Information about the trust store created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTrustStoreOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_stores" in value:
        import aws_sdk_elastic_load_balancing_v2.types.trust_stores

        aws_sdk_elastic_load_balancing_v2.types.trust_stores.serialize_query(
            value["trust_stores"], pairs, f"{prefix}.TrustStores"
        )


def deserialize_query(el: Element) -> CreateTrustStoreOutput:
    out: CreateTrustStoreOutput = {}  # type: ignore[typeddict-item]
    child_trust_stores = el.find("TrustStores")
    if child_trust_stores is not None:
        import aws_sdk_elastic_load_balancing_v2.types.trust_stores

        out["trust_stores"] = (
            aws_sdk_elastic_load_balancing_v2.types.trust_stores.deserialize_query(
                child_trust_stores
            )
        )
    return out
