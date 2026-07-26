"""Generated from Smithy shape ``com.amazonaws.wafv2#ApplicationAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.attribute_name
    import capo_wafv2.types.attribute_values


class ApplicationAttribute(TypedDict, closed=True):
    name: NotRequired["capo_wafv2.types.attribute_name.AttributeName"]
    """<p>Specifies the attribute name.</p>"""
    values: NotRequired["capo_wafv2.types.attribute_values.AttributeValues"]
    """<p>Specifies the attribute value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_wafv2.types.attribute_values

        out["Values"] = capo_wafv2.types.attribute_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationAttribute:
    out: ApplicationAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import capo_wafv2.types.attribute_values

        out["values"] = capo_wafv2.types.attribute_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
