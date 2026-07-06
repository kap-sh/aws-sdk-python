"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntityDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.named_entity_definition_metric
    import aws_sdk_quicksight.types.property_role
    import aws_sdk_quicksight.types.property_usage


class NamedEntityDefinition(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The name of the entity.</p>"""
    property_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The property name to be used for the named entity.</p>"""
    property_role: NotRequired["aws_sdk_quicksight.types.property_role.PropertyRole"]
    """<p>The property role. Valid values for this structure are <code>PRIMARY</code> and <code>ID</code>.</p>"""
    property_usage: NotRequired["aws_sdk_quicksight.types.property_usage.PropertyUsage"]
    """<p>The property usage. Valid values for this structure are <code>INHERIT</code>, <code>DIMENSION</code>, and <code>MEASURE</code>.</p>"""
    metric: NotRequired[
        "aws_sdk_quicksight.types.named_entity_definition_metric.NamedEntityDefinitionMetric"
    ]
    """<p>The definition of a metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamedEntityDefinition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "property_name" in value:
        out["PropertyName"] = value["property_name"]
    if "property_role" in value:
        import aws_sdk_quicksight.types.property_role

        out["PropertyRole"] = aws_sdk_quicksight.types.property_role.serialize_json(
            value["property_role"]
        )
    if "property_usage" in value:
        import aws_sdk_quicksight.types.property_usage

        out["PropertyUsage"] = aws_sdk_quicksight.types.property_usage.serialize_json(
            value["property_usage"]
        )
    if "metric" in value:
        import aws_sdk_quicksight.types.named_entity_definition_metric

        out["Metric"] = (
            aws_sdk_quicksight.types.named_entity_definition_metric.serialize_json(
                value["metric"]
            )
        )
    return out


def deserialize_json(data: dict) -> NamedEntityDefinition:
    out: NamedEntityDefinition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "PropertyName" in data:
        out["property_name"] = data["PropertyName"]
    if "PropertyRole" in data:
        import aws_sdk_quicksight.types.property_role

        out["property_role"] = aws_sdk_quicksight.types.property_role.deserialize_json(
            data["PropertyRole"]
        )
    if "PropertyUsage" in data:
        import aws_sdk_quicksight.types.property_usage

        out["property_usage"] = (
            aws_sdk_quicksight.types.property_usage.deserialize_json(
                data["PropertyUsage"]
            )
        )
    if "Metric" in data:
        import aws_sdk_quicksight.types.named_entity_definition_metric

        out["metric"] = (
            aws_sdk_quicksight.types.named_entity_definition_metric.deserialize_json(
                data["Metric"]
            )
        )
    return out
