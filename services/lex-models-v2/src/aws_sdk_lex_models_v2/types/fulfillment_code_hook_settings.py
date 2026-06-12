"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FulfillmentCodeHookSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boolean
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.fulfillment_updates_specification
    import aws_sdk_lex_models_v2.types.post_fulfillment_status_specification


class FulfillmentCodeHookSettings(TypedDict):
    enabled: "aws_sdk_lex_models_v2.types.boolean.Boolean"
    """<p>Indicates whether a Lambda function should be invoked to fulfill a specific intent.</p>"""
    post_fulfillment_status_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.post_fulfillment_status_specification.PostFulfillmentStatusSpecification"
    ]
    """<p>Provides settings for messages sent to the user for after the Lambda fulfillment function completes. Post-fulfillment messages can be sent for both streaming and non-streaming conversations.</p>"""
    fulfillment_updates_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.fulfillment_updates_specification.FulfillmentUpdatesSpecification"
    ]
    """<p>Provides settings for update messages sent to the user for long-running Lambda fulfillment functions. Fulfillment updates can be used only with streaming conversations.</p>"""
    active: NotRequired["aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Determines whether the fulfillment code hook is used. When <code>active</code> is false, the code hook doesn't run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentCodeHookSettings) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "post_fulfillment_status_specification" in value:
        import aws_sdk_lex_models_v2.types.post_fulfillment_status_specification

        out["postFulfillmentStatusSpecification"] = (
            aws_sdk_lex_models_v2.types.post_fulfillment_status_specification.serialize_json(
                value["post_fulfillment_status_specification"]
            )
        )
    if "fulfillment_updates_specification" in value:
        import aws_sdk_lex_models_v2.types.fulfillment_updates_specification

        out["fulfillmentUpdatesSpecification"] = (
            aws_sdk_lex_models_v2.types.fulfillment_updates_specification.serialize_json(
                value["fulfillment_updates_specification"]
            )
        )
    if "active" in value:
        out["active"] = value["active"]
    return out


def deserialize_json(data: dict) -> FulfillmentCodeHookSettings:
    out: FulfillmentCodeHookSettings = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "postFulfillmentStatusSpecification" in data:
        import aws_sdk_lex_models_v2.types.post_fulfillment_status_specification

        out["post_fulfillment_status_specification"] = (
            aws_sdk_lex_models_v2.types.post_fulfillment_status_specification.deserialize_json(
                data["postFulfillmentStatusSpecification"]
            )
        )
    if "fulfillmentUpdatesSpecification" in data:
        import aws_sdk_lex_models_v2.types.fulfillment_updates_specification

        out["fulfillment_updates_specification"] = (
            aws_sdk_lex_models_v2.types.fulfillment_updates_specification.deserialize_json(
                data["fulfillmentUpdatesSpecification"]
            )
        )
    if "active" in data:
        out["active"] = data["active"]
    return out
