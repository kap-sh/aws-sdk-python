"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#GetTrustStoreRevocationContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.revocation_id
    import aws_sdk_elastic_load_balancing_v2.types.trust_store_arn


class GetTrustStoreRevocationContentInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    revocation_id: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.revocation_id.RevocationId"
    ]
    """<p>The revocation ID of the revocation file.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTrustStoreRevocationContentInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "trust_store_arn" in value:
        pairs.append((f"{prefix}.TrustStoreArn", str(value["trust_store_arn"])))
    if "revocation_id" in value:
        pairs.append((f"{prefix}.RevocationId", str(value["revocation_id"])))


def deserialize_query(el: Element) -> GetTrustStoreRevocationContentInput:
    out: GetTrustStoreRevocationContentInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_revocation_id = el.find("RevocationId")
    if child_revocation_id is not None:
        out["revocation_id"] = int(child_revocation_id.text or "")
    return out
