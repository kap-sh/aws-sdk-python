"""Generated from Smithy shape ``com.amazonaws.wafv2#ApplicationAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.attribute_name
    import aws_sdk_wafv2.types.attribute_values


class ApplicationAttribute(TypedDict):
    name: NotRequired["aws_sdk_wafv2.types.attribute_name.AttributeName"]
    """<p>Specifies the attribute name.</p>"""
    values: NotRequired["aws_sdk_wafv2.types.attribute_values.AttributeValues"]
    """<p>Specifies the attribute value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_wafv2.types.attribute_values

        out["Values"] = aws_sdk_wafv2.types.attribute_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationAttribute:
    out: ApplicationAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_wafv2.types.attribute_values

        out["values"] = aws_sdk_wafv2.types.attribute_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
