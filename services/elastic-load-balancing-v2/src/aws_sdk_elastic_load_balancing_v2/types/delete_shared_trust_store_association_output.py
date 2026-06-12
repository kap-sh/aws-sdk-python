"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteSharedTrustStoreAssociationOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class DeleteSharedTrustStoreAssociationOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSharedTrustStoreAssociationOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteSharedTrustStoreAssociationOutput:
    out: DeleteSharedTrustStoreAssociationOutput = {}  # type: ignore[typeddict-item]
    return out
