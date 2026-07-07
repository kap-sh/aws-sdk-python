"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_filter_key
    import aws_sdk_ssm.types.maintenance_window_filter_values


class MaintenanceWindowFilter(TypedDict, closed=True):
    key: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_filter_key.MaintenanceWindowFilterKey"
    ]
    """<p>The name of the filter.</p>"""
    values: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_filter_values.MaintenanceWindowFilterValues"
    ]
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_ssm.types.maintenance_window_filter_values

        out["Values"] = (
            aws_sdk_ssm.types.maintenance_window_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowFilter:
    out: MaintenanceWindowFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_ssm.types.maintenance_window_filter_values

        out["values"] = (
            aws_sdk_ssm.types.maintenance_window_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
