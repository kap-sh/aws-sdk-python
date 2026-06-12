"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.configuration_event

ConfigurationEventList: TypeAlias = list[
    "aws_sdk_application_insights.types.configuration_event.ConfigurationEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationEventList) -> list:
    import aws_sdk_application_insights.types.configuration_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_insights.types.configuration_event.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationEventList:
    import aws_sdk_application_insights.types.configuration_event

    out: ConfigurationEventList = []
    for item in data:
        out.append(
            aws_sdk_application_insights.types.configuration_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out
