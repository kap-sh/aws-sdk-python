"""Generated from Smithy shape ``com.amazonaws.connect#AssociateBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.lex_bot
    import aws_sdk_connect.types.lex_v2_bot


class AssociateBotRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    lex_bot: NotRequired["aws_sdk_connect.types.lex_bot.LexBot"]
    lex_v2_bot: NotRequired["aws_sdk_connect.types.lex_v2_bot.LexV2Bot"]
    """<p>The Amazon Lex V2 bot to associate with the instance.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateBotRequest) -> dict:
    out: dict = {}
    if "lex_bot" in value:
        import aws_sdk_connect.types.lex_bot

        out["LexBot"] = aws_sdk_connect.types.lex_bot.serialize_json(value["lex_bot"])
    if "lex_v2_bot" in value:
        import aws_sdk_connect.types.lex_v2_bot

        out["LexV2Bot"] = aws_sdk_connect.types.lex_v2_bot.serialize_json(
            value["lex_v2_bot"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateBotRequest:
    out: AssociateBotRequest = {}  # type: ignore[typeddict-item]
    if "LexBot" in data:
        import aws_sdk_connect.types.lex_bot

        out["lex_bot"] = aws_sdk_connect.types.lex_bot.deserialize_json(data["LexBot"])
    if "LexV2Bot" in data:
        import aws_sdk_connect.types.lex_v2_bot

        out["lex_v2_bot"] = aws_sdk_connect.types.lex_v2_bot.deserialize_json(
            data["LexV2Bot"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
