"""Generated from Smithy shape ``com.amazonaws.glue#ExtractedParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_property_key
    import aws_sdk_glue.types.default_value
    import aws_sdk_glue.types.property_location
    import aws_sdk_glue.types.response_extraction_mapping


class ExtractedParameter(TypedDict):
    key: NotRequired["aws_sdk_glue.types.connector_property_key.ConnectorPropertyKey"]
    """<p>The parameter key name that will be used in subsequent requests.</p>"""
    default_value: NotRequired["aws_sdk_glue.types.default_value.DefaultValue"]
    """<p>The default value to use if the parameter cannot be extracted from the response.</p>"""
    property_location: NotRequired[
        "aws_sdk_glue.types.property_location.PropertyLocation"
    ]
    """<p>Specifies where this extracted parameter should be placed in subsequent requests, such as in headers, query parameters, or request body.</p>"""
    value: NotRequired[
        "aws_sdk_glue.types.response_extraction_mapping.ResponseExtractionMapping"
    ]
    """<p>The JSON path or extraction mapping that defines how to extract the parameter value from API responses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtractedParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "property_location" in value:
        import aws_sdk_glue.types.property_location

        out["PropertyLocation"] = (
            aws_sdk_glue.types.property_location.serialize_aws_json_1_1(
                value["property_location"]
            )
        )
    if "value" in value:
        import aws_sdk_glue.types.response_extraction_mapping

        out["Value"] = (
            aws_sdk_glue.types.response_extraction_mapping.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtractedParameter:
    out: ExtractedParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "PropertyLocation" in data:
        import aws_sdk_glue.types.property_location

        out["property_location"] = (
            aws_sdk_glue.types.property_location.deserialize_aws_json_1_1(
                data["PropertyLocation"]
            )
        )
    if "Value" in data:
        import aws_sdk_glue.types.response_extraction_mapping

        out["value"] = (
            aws_sdk_glue.types.response_extraction_mapping.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    return out
