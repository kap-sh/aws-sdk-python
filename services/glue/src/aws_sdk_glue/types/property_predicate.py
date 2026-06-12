"""Generated from Smithy shape ``com.amazonaws.glue#PropertyPredicate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.comparator
    import aws_sdk_glue.types.value_string


class PropertyPredicate(TypedDict):
    key: NotRequired["aws_sdk_glue.types.value_string.ValueString"]
    """<p>The key of the property.</p>"""
    value: NotRequired["aws_sdk_glue.types.value_string.ValueString"]
    """<p>The value of the property.</p>"""
    comparator: NotRequired["aws_sdk_glue.types.comparator.Comparator"]
    """<p>The comparator used to compare this property to others.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyPredicate) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "comparator" in value:
        import aws_sdk_glue.types.comparator

        out["Comparator"] = aws_sdk_glue.types.comparator.serialize_aws_json_1_1(
            value["comparator"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertyPredicate:
    out: PropertyPredicate = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Comparator" in data:
        import aws_sdk_glue.types.comparator

        out["comparator"] = aws_sdk_glue.types.comparator.deserialize_aws_json_1_1(
            data["Comparator"]
        )
    return out
