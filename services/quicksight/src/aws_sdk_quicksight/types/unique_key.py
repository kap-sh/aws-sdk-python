"""Generated from Smithy shape ``com.amazonaws.quicksight#UniqueKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.unique_key_column_name_list


class UniqueKey(TypedDict, closed=True):
    column_names: (
        "aws_sdk_quicksight.types.unique_key_column_name_list.UniqueKeyColumnNameList"
    )
    """<p>The name of the column that is referenced in the <code>UniqueKey</code> configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UniqueKey) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.unique_key_column_name_list

    out["ColumnNames"] = (
        aws_sdk_quicksight.types.unique_key_column_name_list.serialize_json(
            value["column_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> UniqueKey:
    out: UniqueKey = {}  # type: ignore[typeddict-item]
    if "ColumnNames" in data:
        import aws_sdk_quicksight.types.unique_key_column_name_list

        out["column_names"] = (
            aws_sdk_quicksight.types.unique_key_column_name_list.deserialize_json(
                data["ColumnNames"]
            )
        )
    else:
        raise DeserializationError("UniqueKey.column_names required")
    return out
