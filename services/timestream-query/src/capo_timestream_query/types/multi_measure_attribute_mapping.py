"""Generated from Smithy shape ``com.amazonaws.timestreamquery#MultiMeasureAttributeMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.scalar_measure_value_type
    import capo_timestream_query.types.schema_name


class MultiMeasureAttributeMapping(TypedDict, closed=True):
    source_column: "capo_timestream_query.types.schema_name.SchemaName"
    """<p>Source column from where the attribute value is to be read.</p>"""
    target_multi_measure_attribute_name: NotRequired[
        "capo_timestream_query.types.schema_name.SchemaName"
    ]
    """<p>Custom name to be used for attribute name in derived table. If not provided, source column name would be used.</p>"""
    measure_value_type: (
        "capo_timestream_query.types.scalar_measure_value_type.ScalarMeasureValueType"
    )
    """<p>Type of the attribute to be read from the source column.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiMeasureAttributeMapping) -> dict:
    out: dict = {}
    out["SourceColumn"] = value["source_column"]
    if "target_multi_measure_attribute_name" in value:
        out["TargetMultiMeasureAttributeName"] = value[
            "target_multi_measure_attribute_name"
        ]
    import capo_timestream_query.types.scalar_measure_value_type

    out["MeasureValueType"] = (
        capo_timestream_query.types.scalar_measure_value_type.serialize_aws_json_1_0(
            value["measure_value_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultiMeasureAttributeMapping:
    out: MultiMeasureAttributeMapping = {}  # type: ignore[typeddict-item]
    if "SourceColumn" in data:
        out["source_column"] = data["SourceColumn"]
    else:
        raise DeserializationError(
            "MultiMeasureAttributeMapping.source_column required"
        )
    if "TargetMultiMeasureAttributeName" in data:
        out["target_multi_measure_attribute_name"] = data[
            "TargetMultiMeasureAttributeName"
        ]
    if "MeasureValueType" in data:
        import capo_timestream_query.types.scalar_measure_value_type

        out["measure_value_type"] = (
            capo_timestream_query.types.scalar_measure_value_type.deserialize_aws_json_1_0(
                data["MeasureValueType"]
            )
        )
    else:
        raise DeserializationError(
            "MultiMeasureAttributeMapping.measure_value_type required"
        )
    return out
