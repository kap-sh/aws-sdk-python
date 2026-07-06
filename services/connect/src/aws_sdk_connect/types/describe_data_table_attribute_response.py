"""Generated from Smithy shape ``com.amazonaws.connect#DescribeDataTableAttributeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_attribute


class DescribeDataTableAttributeResponse(TypedDict, closed=True):
    attribute: "aws_sdk_connect.types.data_table_attribute.DataTableAttribute"
    """<p>The complete attribute information including configuration, validation rules, lock version, and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataTableAttributeResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_table_attribute

    out["Attribute"] = aws_sdk_connect.types.data_table_attribute.serialize_json(
        value["attribute"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDataTableAttributeResponse:
    out: DescribeDataTableAttributeResponse = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_connect.types.data_table_attribute

        out["attribute"] = aws_sdk_connect.types.data_table_attribute.deserialize_json(
            data["Attribute"]
        )
    else:
        raise DeserializationError(
            "DescribeDataTableAttributeResponse.attribute required"
        )
    return out
