"""Generated from Smithy shape ``com.amazonaws.connect#LexV2Bot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.alias_arn


class LexV2Bot(TypedDict, closed=True):
    alias_arn: NotRequired["aws_sdk_connect.types.alias_arn.AliasArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Lex V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexV2Bot) -> dict:
    out: dict = {}
    if "alias_arn" in value:
        out["AliasArn"] = value["alias_arn"]
    return out


def deserialize_json(data: dict) -> LexV2Bot:
    out: LexV2Bot = {}  # type: ignore[typeddict-item]
    if "AliasArn" in data:
        out["alias_arn"] = data["AliasArn"]
    return out
