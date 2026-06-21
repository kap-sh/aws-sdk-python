"""Generated from Smithy shape ``com.amazonaws.costexplorer#FindingReasonCode``."""

from typing import Literal, TypeAlias, cast

FindingReasonCode: TypeAlias = Literal[
    "CPU_OVER_PROVISIONED",
    "CPU_UNDER_PROVISIONED",
    "MEMORY_OVER_PROVISIONED",
    "MEMORY_UNDER_PROVISIONED",
    "EBS_THROUGHPUT_OVER_PROVISIONED",
    "EBS_THROUGHPUT_UNDER_PROVISIONED",
    "EBS_IOPS_OVER_PROVISIONED",
    "EBS_IOPS_UNDER_PROVISIONED",
    "NETWORK_BANDWIDTH_OVER_PROVISIONED",
    "NETWORK_BANDWIDTH_UNDER_PROVISIONED",
    "NETWORK_PPS_OVER_PROVISIONED",
    "NETWORK_PPS_UNDER_PROVISIONED",
    "DISK_IOPS_OVER_PROVISIONED",
    "DISK_IOPS_UNDER_PROVISIONED",
    "DISK_THROUGHPUT_OVER_PROVISIONED",
    "DISK_THROUGHPUT_UNDER_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FindingReasonCode:
    return cast(FindingReasonCode, data)
