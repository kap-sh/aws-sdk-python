"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeleteTrustStoreOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


class DeleteTrustStoreOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTrustStoreOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteTrustStoreOutput:
    out: DeleteTrustStoreOutput = {}  # type: ignore[typeddict-item]
    return out
