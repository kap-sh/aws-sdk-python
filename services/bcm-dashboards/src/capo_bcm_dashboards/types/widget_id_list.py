"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#WidgetIdList``."""

from typing import TypeAlias

WidgetIdList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WidgetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> WidgetIdList:
    return list(data)
