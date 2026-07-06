"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#InvokedBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.standard_messages
    import aws_sdk_chime_sdk_identity.types.targeted_messages


class InvokedBy(TypedDict, closed=True):
    standard_messages: (
        "aws_sdk_chime_sdk_identity.types.standard_messages.StandardMessages"
    )
    """<p>Sets standard messages as the bot trigger. For standard messages:</p> <ul> <li> <p> <code>ALL</code>: The bot processes all standard messages.</p> </li> <li> <p> <code>AUTO</code>: The bot responds to ALL messages when the channel has one other non-hidden member, and responds to MENTIONS when the channel has more than one other non-hidden member.</p> </li> <li> <p> <code>MENTIONS</code>: The bot processes all standard messages that have a message attribute with <code>CHIME.mentions</code> and a value of the bot ARN.</p> </li> <li> <p> <code>NONE</code>: The bot processes no standard messages.</p> </li> </ul>"""
    targeted_messages: (
        "aws_sdk_chime_sdk_identity.types.targeted_messages.TargetedMessages"
    )
    """<p>Sets targeted messages as the bot trigger. For targeted messages:</p> <ul> <li> <p> <code>ALL</code>: The bot processes all <code>TargetedMessages</code> sent to it. The bot then responds with a targeted message back to the sender. </p> </li> <li> <p> <code>NONE</code>: The bot processes no targeted messages.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokedBy) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_identity.types.standard_messages

    out["StandardMessages"] = (
        aws_sdk_chime_sdk_identity.types.standard_messages.serialize_json(
            value["standard_messages"]
        )
    )
    import aws_sdk_chime_sdk_identity.types.targeted_messages

    out["TargetedMessages"] = (
        aws_sdk_chime_sdk_identity.types.targeted_messages.serialize_json(
            value["targeted_messages"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvokedBy:
    out: InvokedBy = {}  # type: ignore[typeddict-item]
    if "StandardMessages" in data:
        import aws_sdk_chime_sdk_identity.types.standard_messages

        out["standard_messages"] = (
            aws_sdk_chime_sdk_identity.types.standard_messages.deserialize_json(
                data["StandardMessages"]
            )
        )
    else:
        raise DeserializationError("InvokedBy.standard_messages required")
    if "TargetedMessages" in data:
        import aws_sdk_chime_sdk_identity.types.targeted_messages

        out["targeted_messages"] = (
            aws_sdk_chime_sdk_identity.types.targeted_messages.deserialize_json(
                data["TargetedMessages"]
            )
        )
    else:
        raise DeserializationError("InvokedBy.targeted_messages required")
    return out
