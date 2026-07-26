"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetAdministrativeOverrideStateEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

TargetAdministrativeOverrideStateEnum: TypeAlias = Literal[
    "unknown",
    "no_override",
    "zonal_shift_active",
    "zonal_shift_delegated_to_dns",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetAdministrativeOverrideStateEnum) -> str:
    return value


def from_query_text(text: str) -> TargetAdministrativeOverrideStateEnum:
    return cast(TargetAdministrativeOverrideStateEnum, text)


def serialize_query(
    value: TargetAdministrativeOverrideStateEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetAdministrativeOverrideStateEnum:
    return from_query_text(el.text or "")
