"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSemanticDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_descriptive_text


class DataSetSemanticDescription(TypedDict):
    text: "aws_sdk_quicksight.types.data_set_descriptive_text.DataSetDescriptiveText"
    """<p>The descriptive text for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSemanticDescription) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> DataSetSemanticDescription:
    out: DataSetSemanticDescription = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("DataSetSemanticDescription.text required")
    return out
