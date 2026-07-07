"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sensitive_double


class DataSetNumericFilterValue(TypedDict, closed=True):
    static_value: NotRequired[
        "aws_sdk_quicksight.types.sensitive_double.SensitiveDouble"
    ]
    """<p>A static numeric value used for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        out["StaticValue"] = value["static_value"]
    return out


def deserialize_json(data: dict) -> DataSetNumericFilterValue:
    out: DataSetNumericFilterValue = {}  # type: ignore[typeddict-item]
    if "StaticValue" in data:
        out["static_value"] = data["StaticValue"]
    return out
