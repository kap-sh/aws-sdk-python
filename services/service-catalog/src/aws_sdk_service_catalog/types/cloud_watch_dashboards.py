"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CloudWatchDashboards``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.cloud_watch_dashboard

CloudWatchDashboards: TypeAlias = list[
    "aws_sdk_service_catalog.types.cloud_watch_dashboard.CloudWatchDashboard"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchDashboards) -> list:
    import aws_sdk_service_catalog.types.cloud_watch_dashboard

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.cloud_watch_dashboard.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudWatchDashboards:
    import aws_sdk_service_catalog.types.cloud_watch_dashboard

    out: CloudWatchDashboards = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.cloud_watch_dashboard.deserialize_aws_json_1_1(
                item
            )
        )
    return out
