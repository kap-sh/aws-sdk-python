"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AttributeFilter``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_application_signals.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attribute_filter_name
    import aws_sdk_application_signals.types.attribute_filter_values

class AttributeFilter(TypedDict):
    attribute_filter_name: "aws_sdk_application_signals.types.attribute_filter_name.AttributeFilterName"
    """<p>The name of the attribute to filter by, such as <code>Platform</code>, <code>Environment</code>, or <code>BusinessUnit</code>.</p>"""
    attribute_filter_values: "aws_sdk_application_signals.types.attribute_filter_values.AttributeFilterValues"
    """<p>An array of values to match for the specified attribute. Services that have any of these values for the attribute will be included in the results.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilter) -> dict:
    out: dict = {}
    out["AttributeFilterName"] = value["attribute_filter_name"]
    import aws_sdk_application_signals.types.attribute_filter_values
    out["AttributeFilterValues"] = aws_sdk_application_signals.types.attribute_filter_values.serialize_json(value["attribute_filter_values"])
    return out


def deserialize_json(data: dict) -> AttributeFilter:
    out: AttributeFilter = {}  # type: ignore[typeddict-item]
    if "AttributeFilterName" in data:
        out["attribute_filter_name"] = data["AttributeFilterName"]
    else:
        raise DeserializationError("AttributeFilter.attribute_filter_name required")
    if "AttributeFilterValues" in data:
        import aws_sdk_application_signals.types.attribute_filter_values
        out["attribute_filter_values"] = aws_sdk_application_signals.types.attribute_filter_values.deserialize_json(data["AttributeFilterValues"])
    else:
        raise DeserializationError("AttributeFilter.attribute_filter_values required")
    return out