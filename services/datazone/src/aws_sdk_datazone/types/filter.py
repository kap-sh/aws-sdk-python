"""Generated from Smithy shape ``com.amazonaws.datazone#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute
    import aws_sdk_datazone.types.filter_operator


class Filter(TypedDict, closed=True):
    attribute: "aws_sdk_datazone.types.attribute.Attribute"
    """<p>A search filter attribute in Amazon DataZone.</p>"""
    value: "str"
    """<p>A search filter string value in Amazon DataZone.</p>"""
    int_value: NotRequired["int"]
    """<p>A search filter integer value in Amazon DataZone.</p>"""
    operator: "aws_sdk_datazone.types.filter_operator.FilterOperator"
    """<p>Specifies the search filter operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    out["value"] = value.get("value", "")
    if "int_value" in value:
        out["intValue"] = value["int_value"]
    import aws_sdk_datazone.types.filter_operator

    out["operator"] = aws_sdk_datazone.types.filter_operator.serialize_json(
        value.get("operator", "EQ")
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        out["attribute"] = data["attribute"]
    else:
        raise DeserializationError("Filter.attribute required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if "intValue" in data:
        out["int_value"] = data["intValue"]
    if "operator" in data:
        import aws_sdk_datazone.types.filter_operator

        out["operator"] = aws_sdk_datazone.types.filter_operator.deserialize_json(
            data["operator"]
        )
    else:
        out["operator"] = "EQ"
    return out
