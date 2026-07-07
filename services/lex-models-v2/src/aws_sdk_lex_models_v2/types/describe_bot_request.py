"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DescribeBotRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotRequest:
    out: DescribeBotRequest = {}  # type: ignore[typeddict-item]
    return out
