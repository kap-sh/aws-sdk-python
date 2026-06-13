"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksCapacityMonitoringApproach``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

EksCapacityMonitoringApproach: TypeAlias = Literal["sampledMaxInLast24Hours",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("sampledMaxInLast24Hours",))


def serialize_aws_json_1_0(value: EksCapacityMonitoringApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EksCapacityMonitoringApproach:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EksCapacityMonitoringApproach value: {data!r}"
        )
    return cast(EksCapacityMonitoringApproach, data)
