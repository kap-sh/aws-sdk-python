"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddTrustStoreRevocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.revocation_contents
    import aws_sdk_elastic_load_balancing_v2.types.trust_store_arn


class AddTrustStoreRevocationsInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    revocation_contents: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.revocation_contents.RevocationContents"
    ]
    """<p>The revocation file to add.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTrustStoreRevocationsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_store_arn" in value:
        pairs.append((f"{prefix}.TrustStoreArn", str(value["trust_store_arn"])))
    if "revocation_contents" in value:
        import aws_sdk_elastic_load_balancing_v2.types.revocation_contents

        aws_sdk_elastic_load_balancing_v2.types.revocation_contents.serialize_query(
            value["revocation_contents"], pairs, f"{prefix}.RevocationContents"
        )


def deserialize_query(el: Element) -> AddTrustStoreRevocationsInput:
    out: AddTrustStoreRevocationsInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_revocation_contents = el.find("RevocationContents")
    if child_revocation_contents is not None:
        import aws_sdk_elastic_load_balancing_v2.types.revocation_contents

        out["revocation_contents"] = (
            aws_sdk_elastic_load_balancing_v2.types.revocation_contents.deserialize_query(
                child_revocation_contents
            )
        )
    return out
