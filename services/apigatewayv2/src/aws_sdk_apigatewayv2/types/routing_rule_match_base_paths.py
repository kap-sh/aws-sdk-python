"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleMatchBasePaths``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_selection_key


class RoutingRuleMatchBasePaths(TypedDict, closed=True):
    any_of: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_selection_key.__listOfSelectionKey"
    ]
    """The string of the case sensitive base path to be matched."""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleMatchBasePaths) -> dict:
    out: dict = {}
    if "any_of" in value:
        import aws_sdk_apigatewayv2.types.__list_of_selection_key

        out["anyOf"] = (
            aws_sdk_apigatewayv2.types.__list_of_selection_key.serialize_json(
                value["any_of"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingRuleMatchBasePaths:
    out: RoutingRuleMatchBasePaths = {}  # type: ignore[typeddict-item]
    if "anyOf" in data:
        import aws_sdk_apigatewayv2.types.__list_of_selection_key

        out["any_of"] = (
            aws_sdk_apigatewayv2.types.__list_of_selection_key.deserialize_json(
                data["anyOf"]
            )
        )
    return out
