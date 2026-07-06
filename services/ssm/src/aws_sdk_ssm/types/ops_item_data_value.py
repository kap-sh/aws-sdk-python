"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemDataValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_data_type
    import aws_sdk_ssm.types.ops_item_data_value_string


class OpsItemDataValue(TypedDict, closed=True):
    value: NotRequired[
        "aws_sdk_ssm.types.ops_item_data_value_string.OpsItemDataValueString"
    ]
    """<p>The value of the OperationalData key.</p>"""
    type: NotRequired["aws_sdk_ssm.types.ops_item_data_type.OpsItemDataType"]
    """<p>The type of key-value pair. Valid types include <code>SearchableString</code> and <code>String</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemDataValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        import aws_sdk_ssm.types.ops_item_data_type

        out["Type"] = aws_sdk_ssm.types.ops_item_data_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemDataValue:
    out: OpsItemDataValue = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Type" in data:
        import aws_sdk_ssm.types.ops_item_data_type

        out["type"] = aws_sdk_ssm.types.ops_item_data_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
