"""Generated from Smithy shape ``com.amazonaws.connect#AssociateLexBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.lex_bot


class AssociateLexBotRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    lex_bot: "aws_sdk_connect.types.lex_bot.LexBot"
    """<p>The Amazon Lex bot to associate with the instance.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLexBotRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.lex_bot

    out["LexBot"] = aws_sdk_connect.types.lex_bot.serialize_json(value["lex_bot"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateLexBotRequest:
    out: AssociateLexBotRequest = {}  # type: ignore[typeddict-item]
    if "LexBot" in data:
        import aws_sdk_connect.types.lex_bot

        out["lex_bot"] = aws_sdk_connect.types.lex_bot.deserialize_json(data["LexBot"])
    else:
        raise DeserializationError("AssociateLexBotRequest.lex_bot required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
