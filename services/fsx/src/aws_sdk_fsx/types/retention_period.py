"""Generated from Smithy shape ``com.amazonaws.fsx#RetentionPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.retention_period_type
    import aws_sdk_fsx.types.retention_period_value


class RetentionPeriod(TypedDict):
    type: NotRequired["aws_sdk_fsx.types.retention_period_type.RetentionPeriodType"]
    """<p>Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to <code>INFINITE</code>, the files are retained forever. If you set it to <code>UNSPECIFIED</code>, the files are retained until you set an explicit retention period. </p>"""
    value: NotRequired["aws_sdk_fsx.types.retention_period_value.RetentionPeriodValue"]
    """<p>Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You can't set a value for <code>INFINITE</code> or <code>UNSPECIFIED</code>. For all other options, the following ranges are valid: </p> <ul> <li> <p> <code>Seconds</code>: 0 - 65,535</p> </li> <li> <p> <code>Minutes</code>: 0 - 65,535</p> </li> <li> <p> <code>Hours</code>: 0 - 24</p> </li> <li> <p> <code>Days</code>: 0 - 365</p> </li> <li> <p> <code>Months</code>: 0 - 12</p> </li> <li> <p> <code>Years</code>: 0 - 100</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionPeriod) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_fsx.types.retention_period_type

        out["Type"] = aws_sdk_fsx.types.retention_period_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetentionPeriod:
    out: RetentionPeriod = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_fsx.types.retention_period_type

        out["type"] = aws_sdk_fsx.types.retention_period_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
