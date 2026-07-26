"""Generated from Smithy shape ``com.amazonaws.forecast#SchemaAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.attribute_type
    import capo_forecast.types.name


class SchemaAttribute(TypedDict, closed=True):
    attribute_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the dataset field.</p>"""
    attribute_type: NotRequired["capo_forecast.types.attribute_type.AttributeType"]
    """<p>The data type of the field.</p> <p>For a related time series dataset, other than date, item_id, and forecast dimensions attributes, all attributes should be of numerical type (integer/float).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaAttribute) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "attribute_type" in value:
        import capo_forecast.types.attribute_type

        out["AttributeType"] = (
            capo_forecast.types.attribute_type.serialize_aws_json_1_1(
                value["attribute_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaAttribute:
    out: SchemaAttribute = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "AttributeType" in data:
        import capo_forecast.types.attribute_type

        out["attribute_type"] = (
            capo_forecast.types.attribute_type.deserialize_aws_json_1_1(
                data["AttributeType"]
            )
        )
    return out
