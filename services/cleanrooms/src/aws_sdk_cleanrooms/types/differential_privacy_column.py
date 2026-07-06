"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.column_name


class DifferentialPrivacyColumn(TypedDict, closed=True):
    name: "aws_sdk_cleanrooms.types.column_name.ColumnName"
    """<p>The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyColumn) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyColumn:
    out: DifferentialPrivacyColumn = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DifferentialPrivacyColumn.name required")
    return out
