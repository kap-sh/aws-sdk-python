"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sensitive_timestamp


class DataSetDateFilterValue(TypedDict, closed=True):
    static_value: NotRequired[
        "aws_sdk_quicksight.types.sensitive_timestamp.SensitiveTimestamp"
    ]
    """<p>A static date value used for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetDateFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        import aws_sdk_quicksight.types.sensitive_timestamp

        out["StaticValue"] = (
            aws_sdk_quicksight.types.sensitive_timestamp.serialize_json(
                value["static_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetDateFilterValue:
    out: DataSetDateFilterValue = {}  # type: ignore[typeddict-item]
    if "StaticValue" in data:
        import aws_sdk_quicksight.types.sensitive_timestamp

        out["static_value"] = (
            aws_sdk_quicksight.types.sensitive_timestamp.deserialize_json(
                data["StaticValue"]
            )
        )
    return out
