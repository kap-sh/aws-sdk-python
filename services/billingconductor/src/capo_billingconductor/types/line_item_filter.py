"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.attribute_value_list
    import capo_billingconductor.types.line_item_filter_attribute_name
    import capo_billingconductor.types.line_item_filter_values_list
    import capo_billingconductor.types.match_option


class LineItemFilter(TypedDict, closed=True):
    attribute: "capo_billingconductor.types.line_item_filter_attribute_name.LineItemFilterAttributeName"
    """<p>The attribute of the line item filter. This specifies what attribute that you can filter on.</p>"""
    match_option: "capo_billingconductor.types.match_option.MatchOption"
    """<p>The match criteria of the line item filter. This parameter specifies whether not to include the resource value from the billing group total cost.</p>"""
    values: "capo_billingconductor.types.line_item_filter_values_list.LineItemFilterValuesList"
    """<p>The values of the line item filter. This specifies the values to filter on. Currently, you can only exclude Savings Plans discounts.</p>"""
    attribute_values: NotRequired[
        "capo_billingconductor.types.attribute_value_list.AttributeValueList"
    ]
    """<p>The values of the line item filter. This specifies the values to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineItemFilter) -> dict:
    out: dict = {}
    import capo_billingconductor.types.line_item_filter_attribute_name

    out["Attribute"] = (
        capo_billingconductor.types.line_item_filter_attribute_name.serialize_json(
            value["attribute"]
        )
    )
    import capo_billingconductor.types.match_option

    out["MatchOption"] = capo_billingconductor.types.match_option.serialize_json(
        value["match_option"]
    )
    import capo_billingconductor.types.line_item_filter_values_list

    out["Values"] = (
        capo_billingconductor.types.line_item_filter_values_list.serialize_json(
            value.get("values", [])
        )
    )
    if "attribute_values" in value:
        import capo_billingconductor.types.attribute_value_list

        out["AttributeValues"] = (
            capo_billingconductor.types.attribute_value_list.serialize_json(
                value["attribute_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineItemFilter:
    out: LineItemFilter = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import capo_billingconductor.types.line_item_filter_attribute_name

        out["attribute"] = (
            capo_billingconductor.types.line_item_filter_attribute_name.deserialize_json(
                data["Attribute"]
            )
        )
    else:
        raise DeserializationError("LineItemFilter.attribute required")
    if "MatchOption" in data:
        import capo_billingconductor.types.match_option

        out["match_option"] = capo_billingconductor.types.match_option.deserialize_json(
            data["MatchOption"]
        )
    else:
        raise DeserializationError("LineItemFilter.match_option required")
    if "Values" in data:
        import capo_billingconductor.types.line_item_filter_values_list

        out["values"] = (
            capo_billingconductor.types.line_item_filter_values_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if "AttributeValues" in data:
        import capo_billingconductor.types.attribute_value_list

        out["attribute_values"] = (
            capo_billingconductor.types.attribute_value_list.deserialize_json(
                data["AttributeValues"]
            )
        )
    return out
