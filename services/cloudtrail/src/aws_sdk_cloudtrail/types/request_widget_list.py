"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RequestWidgetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.request_widget

RequestWidgetList: TypeAlias = list[
    "aws_sdk_cloudtrail.types.request_widget.RequestWidget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestWidgetList) -> list:
    import aws_sdk_cloudtrail.types.request_widget

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudtrail.types.request_widget.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RequestWidgetList:
    import aws_sdk_cloudtrail.types.request_widget

    out: RequestWidgetList = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.request_widget.deserialize_aws_json_1_1(item)
        )
    return out
