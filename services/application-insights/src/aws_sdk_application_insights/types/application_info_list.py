"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.application_info

ApplicationInfoList: TypeAlias = list[
    "aws_sdk_application_insights.types.application_info.ApplicationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationInfoList) -> list:
    import aws_sdk_application_insights.types.application_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_insights.types.application_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationInfoList:
    import aws_sdk_application_insights.types.application_info

    out: ApplicationInfoList = []
    for item in data:
        out.append(
            aws_sdk_application_insights.types.application_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
