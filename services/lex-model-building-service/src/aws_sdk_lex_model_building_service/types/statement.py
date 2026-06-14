"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Statement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.message_list
    import aws_sdk_lex_model_building_service.types.response_card


class Statement(TypedDict):
    messages: "aws_sdk_lex_model_building_service.types.message_list.MessageList"
    """<p>A collection of message objects.</p>"""
    response_card: NotRequired[
        "aws_sdk_lex_model_building_service.types.response_card.ResponseCard"
    ]
    r"""<p> At runtime, if the client is using the <a href=\"http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\">PostText</a> API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statement) -> dict:
    out: dict = {}
    import aws_sdk_lex_model_building_service.types.message_list

    out["messages"] = (
        aws_sdk_lex_model_building_service.types.message_list.serialize_json(
            value["messages"]
        )
    )
    if "response_card" in value:
        out["responseCard"] = value["response_card"]
    return out


def deserialize_json(data: dict) -> Statement:
    out: Statement = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_lex_model_building_service.types.message_list

        out["messages"] = (
            aws_sdk_lex_model_building_service.types.message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("Statement.messages required")
    if "responseCard" in data:
        out["response_card"] = data["responseCard"]
    return out
