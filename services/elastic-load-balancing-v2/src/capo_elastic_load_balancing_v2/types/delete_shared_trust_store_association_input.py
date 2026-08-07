"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteSharedTrustStoreAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.resource_arn
    import capo_elastic_load_balancing_v2.types.trust_store_arn


class DeleteSharedTrustStoreAssociationInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    resource_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSharedTrustStoreAssociationInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_store_arn" in value:
        pairs.append((f"{key_prefix}TrustStoreArn", str(value["trust_store_arn"])))
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> DeleteSharedTrustStoreAssociationInput:
    out: DeleteSharedTrustStoreAssociationInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out
