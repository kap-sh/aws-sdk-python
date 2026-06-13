"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataColumnProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.synthetic_data_column_name
    import aws_sdk_cleanrooms.types.synthetic_data_column_type


class SyntheticDataColumnProperties(TypedDict):
    column_name: (
        "aws_sdk_cleanrooms.types.synthetic_data_column_name.SyntheticDataColumnName"
    )
    """<p>The name of the data column as it appears in the dataset.</p>"""
    column_type: (
        "aws_sdk_cleanrooms.types.synthetic_data_column_type.SyntheticDataColumnType"
    )
    """<p>The data type of the column, which determines how the synthetic data generation algorithm processes and synthesizes values for this column.</p>"""
    is_predictive_value: "bool"
    """<p>Indicates if this column contains predictive values that should be treated as target variables in machine learning models. This affects how the synthetic data generation preserves statistical relationships.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataColumnProperties) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    import aws_sdk_cleanrooms.types.synthetic_data_column_type

    out["columnType"] = (
        aws_sdk_cleanrooms.types.synthetic_data_column_type.serialize_json(
            value["column_type"]
        )
    )
    out["isPredictiveValue"] = value["is_predictive_value"]
    return out


def deserialize_json(data: dict) -> SyntheticDataColumnProperties:
    out: SyntheticDataColumnProperties = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("SyntheticDataColumnProperties.column_name required")
    if "columnType" in data:
        import aws_sdk_cleanrooms.types.synthetic_data_column_type

        out["column_type"] = (
            aws_sdk_cleanrooms.types.synthetic_data_column_type.deserialize_json(
                data["columnType"]
            )
        )
    else:
        raise DeserializationError("SyntheticDataColumnProperties.column_type required")
    if "isPredictiveValue" in data:
        out["is_predictive_value"] = data["isPredictiveValue"]
    else:
        raise DeserializationError(
            "SyntheticDataColumnProperties.is_predictive_value required"
        )
    return out
