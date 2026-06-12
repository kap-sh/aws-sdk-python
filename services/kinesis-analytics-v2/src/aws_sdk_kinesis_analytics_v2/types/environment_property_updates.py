"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#EnvironmentPropertyUpdates``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.property_groups


class EnvironmentPropertyUpdates(TypedDict):
    property_groups: "aws_sdk_kinesis_analytics_v2.types.property_groups.PropertyGroups"
    """<p>Describes updates to the execution property groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentPropertyUpdates) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.property_groups

    out["PropertyGroups"] = (
        aws_sdk_kinesis_analytics_v2.types.property_groups.serialize_aws_json_1_1(
            value["property_groups"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentPropertyUpdates:
    out: EnvironmentPropertyUpdates = {}  # type: ignore[typeddict-item]
    if "PropertyGroups" in data:
        import aws_sdk_kinesis_analytics_v2.types.property_groups

        out["property_groups"] = (
            aws_sdk_kinesis_analytics_v2.types.property_groups.deserialize_aws_json_1_1(
                data["PropertyGroups"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentPropertyUpdates.property_groups required"
        )
    return out
