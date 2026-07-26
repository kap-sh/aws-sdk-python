"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FulfillmentUpdateResponseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.fulfillment_update_response_frequency
    import capo_lex_models_v2.types.message_groups_list


class FulfillmentUpdateResponseSpecification(TypedDict, closed=True):
    frequency_in_seconds: "capo_lex_models_v2.types.fulfillment_update_response_frequency.FulfillmentUpdateResponseFrequency"
    """<p>The frequency that a message is sent to the user. When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.</p>"""
    message_groups: "capo_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>1 - 5 message groups that contain update messages. Amazon Lex chooses one of the messages to play to the user.</p>"""
    allow_interrupt: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Determines whether the user can interrupt an update message while it is playing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentUpdateResponseSpecification) -> dict:
    out: dict = {}
    out["frequencyInSeconds"] = value["frequency_in_seconds"]
    import capo_lex_models_v2.types.message_groups_list

    out["messageGroups"] = capo_lex_models_v2.types.message_groups_list.serialize_json(
        value["message_groups"]
    )
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    return out


def deserialize_json(data: dict) -> FulfillmentUpdateResponseSpecification:
    out: FulfillmentUpdateResponseSpecification = {}  # type: ignore[typeddict-item]
    if "frequencyInSeconds" in data:
        out["frequency_in_seconds"] = data["frequencyInSeconds"]
    else:
        raise DeserializationError(
            "FulfillmentUpdateResponseSpecification.frequency_in_seconds required"
        )
    if "messageGroups" in data:
        import capo_lex_models_v2.types.message_groups_list

        out["message_groups"] = (
            capo_lex_models_v2.types.message_groups_list.deserialize_json(
                data["messageGroups"]
            )
        )
    else:
        raise DeserializationError(
            "FulfillmentUpdateResponseSpecification.message_groups required"
        )
    if "allowInterrupt" in data:
        out["allow_interrupt"] = data["allowInterrupt"]
    return out
