"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksCapacityMonitoringApproach``."""

from typing import Literal, TypeAlias, cast

EksCapacityMonitoringApproach: TypeAlias = Literal["sampledMaxInLast24Hours",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksCapacityMonitoringApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EksCapacityMonitoringApproach:
    return cast(EksCapacityMonitoringApproach, data)
