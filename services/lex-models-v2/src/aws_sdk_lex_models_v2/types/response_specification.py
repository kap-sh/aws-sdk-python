"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ResponseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.message_groups_list


class ResponseSpecification(TypedDict, closed=True):
    message_groups: "aws_sdk_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.</p>"""
    allow_interrupt: NotRequired[
        "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates whether the user can interrupt a speech response from Amazon Lex.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseSpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.message_groups_list

    out["messageGroups"] = (
        aws_sdk_lex_models_v2.types.message_groups_list.serialize_json(
            value["message_groups"]
        )
    )
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    return out


def deserialize_json(data: dict) -> ResponseSpecification:
    out: ResponseSpecification = {}  # type: ignore[typeddict-item]
    if "messageGroups" in data:
        import aws_sdk_lex_models_v2.types.message_groups_list

        out["message_groups"] = (
            aws_sdk_lex_models_v2.types.message_groups_list.deserialize_json(
                data["messageGroups"]
            )
        )
    else:
        raise DeserializationError("ResponseSpecification.message_groups required")
    if "allowInterrupt" in data:
        out["allow_interrupt"] = data["allowInterrupt"]
    return out
