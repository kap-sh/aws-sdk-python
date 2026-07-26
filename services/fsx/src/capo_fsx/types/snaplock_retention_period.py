"""Generated from Smithy shape ``com.amazonaws.fsx#SnaplockRetentionPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.retention_period


class SnaplockRetentionPeriod(TypedDict, closed=True):
    default_retention: NotRequired["capo_fsx.types.retention_period.RetentionPeriod"]
    """<p>The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period. </p>"""
    minimum_retention: NotRequired["capo_fsx.types.retention_period.RetentionPeriod"]
    """<p>The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume. </p>"""
    maximum_retention: NotRequired["capo_fsx.types.retention_period.RetentionPeriod"]
    """<p>The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnaplockRetentionPeriod) -> dict:
    out: dict = {}
    if "default_retention" in value:
        import capo_fsx.types.retention_period

        out["DefaultRetention"] = (
            capo_fsx.types.retention_period.serialize_aws_json_1_1(
                value["default_retention"]
            )
        )
    if "minimum_retention" in value:
        import capo_fsx.types.retention_period

        out["MinimumRetention"] = (
            capo_fsx.types.retention_period.serialize_aws_json_1_1(
                value["minimum_retention"]
            )
        )
    if "maximum_retention" in value:
        import capo_fsx.types.retention_period

        out["MaximumRetention"] = (
            capo_fsx.types.retention_period.serialize_aws_json_1_1(
                value["maximum_retention"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnaplockRetentionPeriod:
    out: SnaplockRetentionPeriod = {}  # type: ignore[typeddict-item]
    if "DefaultRetention" in data:
        import capo_fsx.types.retention_period

        out["default_retention"] = (
            capo_fsx.types.retention_period.deserialize_aws_json_1_1(
                data["DefaultRetention"]
            )
        )
    if "MinimumRetention" in data:
        import capo_fsx.types.retention_period

        out["minimum_retention"] = (
            capo_fsx.types.retention_period.deserialize_aws_json_1_1(
                data["MinimumRetention"]
            )
        )
    if "MaximumRetention" in data:
        import capo_fsx.types.retention_period

        out["maximum_retention"] = (
            capo_fsx.types.retention_period.deserialize_aws_json_1_1(
                data["MaximumRetention"]
            )
        )
    return out
