"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#FulfillmentActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.code_hook
    import aws_sdk_lex_model_building_service.types.fulfillment_activity_type


class FulfillmentActivity(TypedDict, closed=True):
    type: "aws_sdk_lex_model_building_service.types.fulfillment_activity_type.FulfillmentActivityType"
    """<p> How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application. </p>"""
    code_hook: NotRequired[
        "aws_sdk_lex_model_building_service.types.code_hook.CodeHook"
    ]
    """<p> A description of the Lambda function that is run to fulfill the intent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentActivity) -> dict:
    out: dict = {}
    import aws_sdk_lex_model_building_service.types.fulfillment_activity_type

    out["type"] = (
        aws_sdk_lex_model_building_service.types.fulfillment_activity_type.serialize_json(
            value["type"]
        )
    )
    if "code_hook" in value:
        import aws_sdk_lex_model_building_service.types.code_hook

        out["codeHook"] = (
            aws_sdk_lex_model_building_service.types.code_hook.serialize_json(
                value["code_hook"]
            )
        )
    return out


def deserialize_json(data: dict) -> FulfillmentActivity:
    out: FulfillmentActivity = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_lex_model_building_service.types.fulfillment_activity_type

        out["type"] = (
            aws_sdk_lex_model_building_service.types.fulfillment_activity_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("FulfillmentActivity.type required")
    if "codeHook" in data:
        import aws_sdk_lex_model_building_service.types.code_hook

        out["code_hook"] = (
            aws_sdk_lex_model_building_service.types.code_hook.deserialize_json(
                data["codeHook"]
            )
        )
    return out
