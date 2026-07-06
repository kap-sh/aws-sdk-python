"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FulfillmentStartResponseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.fulfillment_start_response_delay
    import aws_sdk_lex_models_v2.types.message_groups_list


class FulfillmentStartResponseSpecification(TypedDict, closed=True):
    delay_in_seconds: "aws_sdk_lex_models_v2.types.fulfillment_start_response_delay.FulfillmentStartResponseDelay"
    """<p>The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isn't played.</p>"""
    message_groups: "aws_sdk_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.</p>"""
    allow_interrupt: NotRequired[
        "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Determines whether the user can interrupt the start message while it is playing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentStartResponseSpecification) -> dict:
    out: dict = {}
    out["delayInSeconds"] = value["delay_in_seconds"]
    import aws_sdk_lex_models_v2.types.message_groups_list

    out["messageGroups"] = (
        aws_sdk_lex_models_v2.types.message_groups_list.serialize_json(
            value["message_groups"]
        )
    )
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    return out


def deserialize_json(data: dict) -> FulfillmentStartResponseSpecification:
    out: FulfillmentStartResponseSpecification = {}  # type: ignore[typeddict-item]
    if "delayInSeconds" in data:
        out["delay_in_seconds"] = data["delayInSeconds"]
    else:
        raise DeserializationError(
            "FulfillmentStartResponseSpecification.delay_in_seconds required"
        )
    if "messageGroups" in data:
        import aws_sdk_lex_models_v2.types.message_groups_list

        out["message_groups"] = (
            aws_sdk_lex_models_v2.types.message_groups_list.deserialize_json(
                data["messageGroups"]
            )
        )
    else:
        raise DeserializationError(
            "FulfillmentStartResponseSpecification.message_groups required"
        )
    if "allowInterrupt" in data:
        out["allow_interrupt"] = data["allowInterrupt"]
    return out
