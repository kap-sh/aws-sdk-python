"""Generated from Smithy shape ``com.amazonaws.costexplorer#DimensionValuesWithAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.attributes
    import aws_sdk_cost_explorer.types.value


class DimensionValuesWithAttributes(TypedDict, closed=True):
    value: NotRequired["aws_sdk_cost_explorer.types.value.Value"]
    """<p>The value of a dimension with a specific attribute.</p>"""
    attributes: NotRequired["aws_sdk_cost_explorer.types.attributes.Attributes"]
    """<p>The attribute that applies to a specific <code>Dimension</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionValuesWithAttributes) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "attributes" in value:
        import aws_sdk_cost_explorer.types.attributes

        out["Attributes"] = (
            aws_sdk_cost_explorer.types.attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionValuesWithAttributes:
    out: DimensionValuesWithAttributes = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Attributes" in data:
        import aws_sdk_cost_explorer.types.attributes

        out["attributes"] = (
            aws_sdk_cost_explorer.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
