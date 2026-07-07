"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#EnvironmentProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.property_groups


class EnvironmentProperties(TypedDict, closed=True):
    property_groups: "aws_sdk_kinesis_analytics_v2.types.property_groups.PropertyGroups"
    """<p>Describes the execution property groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentProperties) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.property_groups

    out["PropertyGroups"] = (
        aws_sdk_kinesis_analytics_v2.types.property_groups.serialize_aws_json_1_1(
            value["property_groups"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentProperties:
    out: EnvironmentProperties = {}  # type: ignore[typeddict-item]
    if "PropertyGroups" in data:
        import aws_sdk_kinesis_analytics_v2.types.property_groups

        out["property_groups"] = (
            aws_sdk_kinesis_analytics_v2.types.property_groups.deserialize_aws_json_1_1(
                data["PropertyGroups"]
            )
        )
    else:
        raise DeserializationError("EnvironmentProperties.property_groups required")
    return out
