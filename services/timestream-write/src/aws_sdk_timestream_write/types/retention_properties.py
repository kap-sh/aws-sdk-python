"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#RetentionProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.magnetic_store_retention_period_in_days
    import aws_sdk_timestream_write.types.memory_store_retention_period_in_hours


class RetentionProperties(TypedDict):
    memory_store_retention_period_in_hours: "aws_sdk_timestream_write.types.memory_store_retention_period_in_hours.MemoryStoreRetentionPeriodInHours"
    """<p>The duration for which data must be stored in the memory store. </p>"""
    magnetic_store_retention_period_in_days: "aws_sdk_timestream_write.types.magnetic_store_retention_period_in_days.MagneticStoreRetentionPeriodInDays"
    """<p>The duration for which data must be stored in the magnetic store. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetentionProperties) -> dict:
    out: dict = {}
    out["MemoryStoreRetentionPeriodInHours"] = value[
        "memory_store_retention_period_in_hours"
    ]
    out["MagneticStoreRetentionPeriodInDays"] = value[
        "magnetic_store_retention_period_in_days"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> RetentionProperties:
    out: RetentionProperties = {}  # type: ignore[typeddict-item]
    if "MemoryStoreRetentionPeriodInHours" in data:
        out["memory_store_retention_period_in_hours"] = data[
            "MemoryStoreRetentionPeriodInHours"
        ]
    else:
        raise DeserializationError(
            "RetentionProperties.memory_store_retention_period_in_hours required"
        )
    if "MagneticStoreRetentionPeriodInDays" in data:
        out["magnetic_store_retention_period_in_days"] = data[
            "MagneticStoreRetentionPeriodInDays"
        ]
    else:
        raise DeserializationError(
            "RetentionProperties.magnetic_store_retention_period_in_days required"
        )
    return out
