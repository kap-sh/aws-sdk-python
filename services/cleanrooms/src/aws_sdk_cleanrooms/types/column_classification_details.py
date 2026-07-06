"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ColumnClassificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.column_mapping_list


class ColumnClassificationDetails(TypedDict, closed=True):
    column_mapping: "aws_sdk_cleanrooms.types.column_mapping_list.ColumnMappingList"
    """<p>A mapping that defines the classification of data columns for synthetic data generation and specifies how each column should be handled during the privacy-preserving data synthesis process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnClassificationDetails) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.column_mapping_list

    out["columnMapping"] = aws_sdk_cleanrooms.types.column_mapping_list.serialize_json(
        value["column_mapping"]
    )
    return out


def deserialize_json(data: dict) -> ColumnClassificationDetails:
    out: ColumnClassificationDetails = {}  # type: ignore[typeddict-item]
    if "columnMapping" in data:
        import aws_sdk_cleanrooms.types.column_mapping_list

        out["column_mapping"] = (
            aws_sdk_cleanrooms.types.column_mapping_list.deserialize_json(
                data["columnMapping"]
            )
        )
    else:
        raise DeserializationError(
            "ColumnClassificationDetails.column_mapping required"
        )
    return out
