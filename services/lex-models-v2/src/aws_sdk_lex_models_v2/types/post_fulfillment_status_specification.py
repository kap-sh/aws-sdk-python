"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PostFulfillmentStatusSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conditional_specification
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.response_specification


class PostFulfillmentStatusSpecification(TypedDict, closed=True):
    success_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    failure_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    timeout_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    success_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.</p>"""
    success_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.</p>"""
    failure_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the <code>State</code> field of the <code>Intent</code> object set to <code>Failed</code>.</p>"""
    failure_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the <code>State</code> field of the <code>Intent</code> object set to <code>Failed</code>.</p>"""
    timeout_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot runs when the fulfillment code hook times out.</p>"""
    timeout_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate if the fulfillment code hook times out.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostFulfillmentStatusSpecification) -> dict:
    out: dict = {}
    if "success_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["successResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["success_response"]
            )
        )
    if "failure_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["failureResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["failure_response"]
            )
        )
    if "timeout_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["timeoutResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["timeout_response"]
            )
        )
    if "success_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["successNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["success_next_step"]
            )
        )
    if "success_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["successConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["success_conditional"]
            )
        )
    if "failure_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["failureNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["failure_next_step"]
            )
        )
    if "failure_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["failureConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["failure_conditional"]
            )
        )
    if "timeout_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["timeoutNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["timeout_next_step"]
            )
        )
    if "timeout_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["timeoutConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["timeout_conditional"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostFulfillmentStatusSpecification:
    out: PostFulfillmentStatusSpecification = {}  # type: ignore[typeddict-item]
    if "successResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["success_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["successResponse"]
            )
        )
    if "failureResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["failure_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["failureResponse"]
            )
        )
    if "timeoutResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["timeout_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["timeoutResponse"]
            )
        )
    if "successNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["success_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["successNextStep"]
            )
        )
    if "successConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["success_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["successConditional"]
            )
        )
    if "failureNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["failure_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["failureNextStep"]
            )
        )
    if "failureConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["failure_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["failureConditional"]
            )
        )
    if "timeoutNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["timeout_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["timeoutNextStep"]
            )
        )
    if "timeoutConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["timeout_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["timeoutConditional"]
            )
        )
    return out
