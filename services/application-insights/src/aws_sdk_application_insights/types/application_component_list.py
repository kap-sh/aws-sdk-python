"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.application_component

ApplicationComponentList: TypeAlias = list[
    "aws_sdk_application_insights.types.application_component.ApplicationComponent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationComponentList) -> list:
    import aws_sdk_application_insights.types.application_component

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_insights.types.application_component.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationComponentList:
    import aws_sdk_application_insights.types.application_component

    out: ApplicationComponentList = []
    for item in data:
        out.append(
            aws_sdk_application_insights.types.application_component.deserialize_aws_json_1_1(
                item
            )
        )
    return out
