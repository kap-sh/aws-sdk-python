"""Generated from Smithy shape ``com.amazonaws.redshift#UsageLimitFeatureType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

UsageLimitFeatureType: TypeAlias = Literal[
    "spectrum",
    "concurrency-scaling",
    "cross-region-datasharing",
    "extra-compute-for-automatic-optimization",
]


# --- awsQuery ser/de ---
def to_query_text(value: UsageLimitFeatureType) -> str:
    return value


def from_query_text(text: str) -> UsageLimitFeatureType:
    return cast(UsageLimitFeatureType, text)


def serialize_query(
    value: UsageLimitFeatureType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UsageLimitFeatureType:
    return from_query_text(el.text or "")
