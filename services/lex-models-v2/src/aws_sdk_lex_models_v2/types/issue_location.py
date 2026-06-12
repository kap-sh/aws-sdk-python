"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IssueLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class IssueLocation(TypedDict):
    bot_locale: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier where the issue was found.</p>"""
    intent_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The intent identifier where the issue was found, if applicable.</p>"""
    slot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The slot identifier where the issue was found, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueLocation) -> dict:
    out: dict = {}
    if "bot_locale" in value:
        out["botLocale"] = value["bot_locale"]
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "slot_id" in value:
        out["slotId"] = value["slot_id"]
    return out


def deserialize_json(data: dict) -> IssueLocation:
    out: IssueLocation = {}  # type: ignore[typeddict-item]
    if "botLocale" in data:
        out["bot_locale"] = data["botLocale"]
    if "intentId" in data:
        out["intent_id"] = data["intentId"]
    if "slotId" in data:
        out["slot_id"] = data["slotId"]
    return out
