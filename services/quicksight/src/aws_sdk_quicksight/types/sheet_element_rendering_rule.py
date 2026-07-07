"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetElementRenderingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.sheet_element_configuration_overrides


class SheetElementRenderingRule(TypedDict, closed=True):
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The expression of the rendering rules of a sheet.</p>"""
    configuration_overrides: "aws_sdk_quicksight.types.sheet_element_configuration_overrides.SheetElementConfigurationOverrides"
    """<p>The override configuration of the rendering rules of a sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetElementRenderingRule) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import aws_sdk_quicksight.types.sheet_element_configuration_overrides

    out["ConfigurationOverrides"] = (
        aws_sdk_quicksight.types.sheet_element_configuration_overrides.serialize_json(
            value["configuration_overrides"]
        )
    )
    return out


def deserialize_json(data: dict) -> SheetElementRenderingRule:
    out: SheetElementRenderingRule = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("SheetElementRenderingRule.expression required")
    if "ConfigurationOverrides" in data:
        import aws_sdk_quicksight.types.sheet_element_configuration_overrides

        out["configuration_overrides"] = (
            aws_sdk_quicksight.types.sheet_element_configuration_overrides.deserialize_json(
                data["ConfigurationOverrides"]
            )
        )
    else:
        raise DeserializationError(
            "SheetElementRenderingRule.configuration_overrides required"
        )
    return out
