"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetAdministrativeOverrideReasonEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TargetAdministrativeOverrideReasonEnum: TypeAlias = Literal[
    "AdministrativeOverride.Unknown",
    "AdministrativeOverride.NoOverride",
    "AdministrativeOverride.ZonalShiftActive",
    "AdministrativeOverride.ZonalShiftDelegatedToDns",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AdministrativeOverride.Unknown",
        "AdministrativeOverride.NoOverride",
        "AdministrativeOverride.ZonalShiftActive",
        "AdministrativeOverride.ZonalShiftDelegatedToDns",
    )
)


def to_query_text(value: TargetAdministrativeOverrideReasonEnum) -> str:
    return value


def from_query_text(text: str) -> TargetAdministrativeOverrideReasonEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TargetAdministrativeOverrideReasonEnum value: {text!r}"
        )
    return cast(TargetAdministrativeOverrideReasonEnum, text)


def serialize_query(
    value: TargetAdministrativeOverrideReasonEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetAdministrativeOverrideReasonEnum:
    return from_query_text(el.text or "")
