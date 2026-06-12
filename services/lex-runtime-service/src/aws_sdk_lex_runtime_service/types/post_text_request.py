"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PostTextRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.active_contexts_list
    import aws_sdk_lex_runtime_service.types.bot_alias
    import aws_sdk_lex_runtime_service.types.bot_name
    import aws_sdk_lex_runtime_service.types.string_map
    import aws_sdk_lex_runtime_service.types.text
    import aws_sdk_lex_runtime_service.types.user_id


class PostTextRequest(TypedDict):
    bot_name: "aws_sdk_lex_runtime_service.types.bot_name.BotName"
    """<p>The name of the Amazon Lex bot.</p>"""
    bot_alias: "aws_sdk_lex_runtime_service.types.bot_alias.BotAlias"
    """<p>The alias of the Amazon Lex bot.</p>"""
    user_id: "aws_sdk_lex_runtime_service.types.user_id.UserId"
    """<p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the <code>userID</code> field.</p> <p>To decide the user ID to use for your application, consider the following factors.</p> <ul> <li> <p>The <code>userID</code> field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.</p> </li> <li> <p>If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.</p> </li> <li> <p>If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.</p> </li> <li> <p>A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.</p> </li> </ul>"""
    session_attributes: NotRequired[
        "aws_sdk_lex_runtime_service.types.string_map.StringMap"
    ]
    """<p>Application-specific information passed between Amazon Lex and a client application.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs\">Setting Session Attributes</a>.</p>"""
    request_attributes: NotRequired[
        "aws_sdk_lex_runtime_service.types.string_map.StringMap"
    ]
    """<p>Request-specific information passed between Amazon Lex and a client application.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs\">Setting Request Attributes</a>.</p>"""
    input_text: "aws_sdk_lex_runtime_service.types.text.Text"
    """<p>The text that the user entered (Amazon Lex interprets this text).</p>"""
    active_contexts: NotRequired[
        "aws_sdk_lex_runtime_service.types.active_contexts_list.ActiveContextsList"
    ]
    """<p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,</p> <p>If you don't specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostTextRequest) -> dict:
    out: dict = {}
    if "session_attributes" in value:
        import aws_sdk_lex_runtime_service.types.string_map

        out["sessionAttributes"] = (
            aws_sdk_lex_runtime_service.types.string_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "request_attributes" in value:
        import aws_sdk_lex_runtime_service.types.string_map

        out["requestAttributes"] = (
            aws_sdk_lex_runtime_service.types.string_map.serialize_json(
                value["request_attributes"]
            )
        )
    out["inputText"] = value["input_text"]
    if "active_contexts" in value:
        import aws_sdk_lex_runtime_service.types.active_contexts_list

        out["activeContexts"] = (
            aws_sdk_lex_runtime_service.types.active_contexts_list.serialize_json(
                value["active_contexts"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostTextRequest:
    out: PostTextRequest = {}  # type: ignore[typeddict-item]
    if "sessionAttributes" in data:
        import aws_sdk_lex_runtime_service.types.string_map

        out["session_attributes"] = (
            aws_sdk_lex_runtime_service.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if "requestAttributes" in data:
        import aws_sdk_lex_runtime_service.types.string_map

        out["request_attributes"] = (
            aws_sdk_lex_runtime_service.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    if "inputText" in data:
        out["input_text"] = data["inputText"]
    else:
        raise DeserializationError("PostTextRequest.input_text required")
    if "activeContexts" in data:
        import aws_sdk_lex_runtime_service.types.active_contexts_list

        out["active_contexts"] = (
            aws_sdk_lex_runtime_service.types.active_contexts_list.deserialize_json(
                data["activeContexts"]
            )
        )
    return out
