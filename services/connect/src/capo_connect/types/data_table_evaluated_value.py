"""Generated from Smithy shape ``com.amazonaws.connect#DataTableEvaluatedValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.data_table_attribute_value_type
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_set
    import capo_connect.types.string


class DataTableEvaluatedValue(TypedDict, closed=True):
    record_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The value's record ID.</p>"""
    primary_values: "capo_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The value's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The value's attribute name.</p>"""
    value_type: (
        "capo_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    )
    """<p>The value's value type.</p>"""
    found: "capo_connect.types.boolean.Boolean"
    """<p>The value's found.</p>"""
    error: "capo_connect.types.boolean.Boolean"
    """<p>The value's error.</p>"""
    evaluated_value: "capo_connect.types.string.String"
    """<p>The value's evaluated value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableEvaluatedValue) -> dict:
    out: dict = {}
    out["RecordId"] = value["record_id"]
    import capo_connect.types.primary_values_set

    out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    out["AttributeName"] = value["attribute_name"]
    import capo_connect.types.data_table_attribute_value_type

    out["ValueType"] = (
        capo_connect.types.data_table_attribute_value_type.serialize_json(
            value["value_type"]
        )
    )
    out["Found"] = value.get("found", False)
    out["Error"] = value.get("error", False)
    out["EvaluatedValue"] = value["evaluated_value"]
    return out


def deserialize_json(data: dict) -> DataTableEvaluatedValue:
    out: DataTableEvaluatedValue = {}  # type: ignore[typeddict-item]
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    else:
        raise DeserializationError("DataTableEvaluatedValue.record_id required")
    if "PrimaryValues" in data:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    else:
        raise DeserializationError("DataTableEvaluatedValue.primary_values required")
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("DataTableEvaluatedValue.attribute_name required")
    if "ValueType" in data:
        import capo_connect.types.data_table_attribute_value_type

        out["value_type"] = (
            capo_connect.types.data_table_attribute_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError("DataTableEvaluatedValue.value_type required")
    if "Found" in data:
        out["found"] = data["Found"]
    else:
        out["found"] = False
    if "Error" in data:
        out["error"] = data["Error"]
    else:
        out["error"] = False
    if "EvaluatedValue" in data:
        out["evaluated_value"] = data["EvaluatedValue"]
    else:
        raise DeserializationError("DataTableEvaluatedValue.evaluated_value required")
    return out
