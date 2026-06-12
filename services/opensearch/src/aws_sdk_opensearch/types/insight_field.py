"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.insight_field_type
    import aws_sdk_opensearch.types.string


class InsightField(TypedDict):
    name: "aws_sdk_opensearch.types.string.String"
    """<p>The name of the insight field.</p>"""
    type: "aws_sdk_opensearch.types.insight_field_type.InsightFieldType"
    """<p>The type of the insight field. Possible values are <code>text</code> and <code>metric</code>.</p>"""
    value: "aws_sdk_opensearch.types.string.String"
    """<p>The value of the insight field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_opensearch.types.insight_field_type

    out["Type"] = aws_sdk_opensearch.types.insight_field_type.serialize_json(
        value["type"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> InsightField:
    out: InsightField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("InsightField.name required")
    if "Type" in data:
        import aws_sdk_opensearch.types.insight_field_type

        out["type"] = aws_sdk_opensearch.types.insight_field_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("InsightField.type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("InsightField.value required")
    return out
