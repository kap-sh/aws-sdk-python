"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#EnvironmentPropertyDescriptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.property_groups


class EnvironmentPropertyDescriptions(TypedDict, closed=True):
    property_group_descriptions: NotRequired[
        "capo_kinesis_analytics_v2.types.property_groups.PropertyGroups"
    ]
    """<p>Describes the execution property groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentPropertyDescriptions) -> dict:
    out: dict = {}
    if "property_group_descriptions" in value:
        import capo_kinesis_analytics_v2.types.property_groups

        out["PropertyGroupDescriptions"] = (
            capo_kinesis_analytics_v2.types.property_groups.serialize_aws_json_1_1(
                value["property_group_descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentPropertyDescriptions:
    out: EnvironmentPropertyDescriptions = {}  # type: ignore[typeddict-item]
    if "PropertyGroupDescriptions" in data:
        import capo_kinesis_analytics_v2.types.property_groups

        out["property_group_descriptions"] = (
            capo_kinesis_analytics_v2.types.property_groups.deserialize_aws_json_1_1(
                data["PropertyGroupDescriptions"]
            )
        )
    return out
