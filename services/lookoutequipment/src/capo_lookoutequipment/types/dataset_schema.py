"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DatasetSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.synthesized_json_inline_data_schema


class DatasetSchema(TypedDict, closed=True):
    inline_data_schema: NotRequired[
        "capo_lookoutequipment.types.synthesized_json_inline_data_schema.SynthesizedJsonInlineDataSchema"
    ]
    """<p>The data schema used within the given dataset.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatasetSchema) -> dict:
    out: dict = {}
    if "inline_data_schema" in value:
        out["InlineDataSchema"] = value["inline_data_schema"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DatasetSchema:
    out: DatasetSchema = {}  # type: ignore[typeddict-item]
    if "InlineDataSchema" in data:
        out["inline_data_schema"] = data["InlineDataSchema"]
    return out
