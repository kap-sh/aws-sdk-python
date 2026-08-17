"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemDataValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_data_type
    import capo_ssm.types.ops_item_data_value_string


class OpsItemDataValue(TypedDict, closed=True):
    value: NotRequired[
        "capo_ssm.types.ops_item_data_value_string.OpsItemDataValueString"
    ]
    """<p>The value of the OperationalData key.</p>"""
    type: NotRequired["capo_ssm.types.ops_item_data_type.OpsItemDataType"]
    """<p>The type of key-value pair. Valid types include <code>SearchableString</code> and <code>String</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemDataValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        import capo_ssm.types.ops_item_data_type

        out["Type"] = capo_ssm.types.ops_item_data_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemDataValue:
    out: OpsItemDataValue = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Type") is not None:
        import capo_ssm.types.ops_item_data_type

        out["type"] = capo_ssm.types.ops_item_data_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
