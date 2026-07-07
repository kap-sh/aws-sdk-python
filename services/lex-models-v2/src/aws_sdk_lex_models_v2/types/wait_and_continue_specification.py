"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#WaitAndContinueSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.response_specification
    import aws_sdk_lex_models_v2.types.still_waiting_response_specification


class WaitAndContinueSpecification(TypedDict, closed=True):
    waiting_response: (
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    )
    """<p>The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.</p>"""
    continue_response: (
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    )
    """<p>The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.</p>"""
    still_waiting_response: NotRequired[
        "aws_sdk_lex_models_v2.types.still_waiting_response_specification.StillWaitingResponseSpecification"
    ]
    """<p>A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.</p>"""
    active: NotRequired["aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot aren't used. If the <code>active</code> field isn't specified, the default is true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitAndContinueSpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.response_specification

    out["waitingResponse"] = (
        aws_sdk_lex_models_v2.types.response_specification.serialize_json(
            value["waiting_response"]
        )
    )
    import aws_sdk_lex_models_v2.types.response_specification

    out["continueResponse"] = (
        aws_sdk_lex_models_v2.types.response_specification.serialize_json(
            value["continue_response"]
        )
    )
    if "still_waiting_response" in value:
        import aws_sdk_lex_models_v2.types.still_waiting_response_specification

        out["stillWaitingResponse"] = (
            aws_sdk_lex_models_v2.types.still_waiting_response_specification.serialize_json(
                value["still_waiting_response"]
            )
        )
    if "active" in value:
        out["active"] = value["active"]
    return out


def deserialize_json(data: dict) -> WaitAndContinueSpecification:
    out: WaitAndContinueSpecification = {}  # type: ignore[typeddict-item]
    if "waitingResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["waiting_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["waitingResponse"]
            )
        )
    else:
        raise DeserializationError(
            "WaitAndContinueSpecification.waiting_response required"
        )
    if "continueResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["continue_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["continueResponse"]
            )
        )
    else:
        raise DeserializationError(
            "WaitAndContinueSpecification.continue_response required"
        )
    if "stillWaitingResponse" in data:
        import aws_sdk_lex_models_v2.types.still_waiting_response_specification

        out["still_waiting_response"] = (
            aws_sdk_lex_models_v2.types.still_waiting_response_specification.deserialize_json(
                data["stillWaitingResponse"]
            )
        )
    if "active" in data:
        out["active"] = data["active"]
    return out
