"""Generated from Smithy shape ``com.amazonaws.rbin#RetentionPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rbin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rbin.types.retention_period_unit
    import aws_sdk_rbin.types.retention_period_value


class RetentionPeriod(TypedDict):
    retention_period_value: (
        "aws_sdk_rbin.types.retention_period_value.RetentionPeriodValue"
    )
    """<p>The period value for which the retention rule is to retain resources, measured in days. The supported retention periods are:</p> <ul> <li> <p>EBS volumes: 1 - 7 days</p> </li> <li> <p>EBS snapshots and EBS-backed AMIs: 1 - 365 days</p> </li> </ul>"""
    retention_period_unit: (
        "aws_sdk_rbin.types.retention_period_unit.RetentionPeriodUnit"
    )
    """<p>The unit of time in which the retention period is measured. Currently, only <code>DAYS</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetentionPeriod) -> dict:
    out: dict = {}
    out["RetentionPeriodValue"] = value["retention_period_value"]
    import aws_sdk_rbin.types.retention_period_unit

    out["RetentionPeriodUnit"] = (
        aws_sdk_rbin.types.retention_period_unit.serialize_json(
            value["retention_period_unit"]
        )
    )
    return out


def deserialize_json(data: dict) -> RetentionPeriod:
    out: RetentionPeriod = {}  # type: ignore[typeddict-item]
    if "RetentionPeriodValue" in data:
        out["retention_period_value"] = data["RetentionPeriodValue"]
    else:
        raise DeserializationError("RetentionPeriod.retention_period_value required")
    if "RetentionPeriodUnit" in data:
        import aws_sdk_rbin.types.retention_period_unit

        out["retention_period_unit"] = (
            aws_sdk_rbin.types.retention_period_unit.deserialize_json(
                data["RetentionPeriodUnit"]
            )
        )
    else:
        raise DeserializationError("RetentionPeriod.retention_period_unit required")
    return out
