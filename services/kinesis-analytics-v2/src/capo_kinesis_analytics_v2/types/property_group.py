"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#PropertyGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.property_map


class PropertyGroup(TypedDict, closed=True):
    property_group_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>Describes the key of an application execution property key-value pair.</p>"""
    property_map: "capo_kinesis_analytics_v2.types.property_map.PropertyMap"
    """<p>Describes the value of an application execution property key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyGroup) -> dict:
    out: dict = {}
    out["PropertyGroupId"] = value["property_group_id"]
    import capo_kinesis_analytics_v2.types.property_map

    out["PropertyMap"] = (
        capo_kinesis_analytics_v2.types.property_map.serialize_aws_json_1_1(
            value["property_map"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertyGroup:
    out: PropertyGroup = {}  # type: ignore[typeddict-item]
    if "PropertyGroupId" in data:
        out["property_group_id"] = data["PropertyGroupId"]
    else:
        raise DeserializationError("PropertyGroup.property_group_id required")
    if "PropertyMap" in data:
        import capo_kinesis_analytics_v2.types.property_map

        out["property_map"] = (
            capo_kinesis_analytics_v2.types.property_map.deserialize_aws_json_1_1(
                data["PropertyMap"]
            )
        )
    else:
        raise DeserializationError("PropertyGroup.property_map required")
    return out
