"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalysisScope``."""

from typing import Literal, TypeAlias, cast

"""<p>The scope of analysis to perform on the bot.</p> <p>Valid values include:</p> <ul> <li> <p> <code>BotLocale</code> </p> </li> </ul>"""
AnalysisScope: TypeAlias = Literal["BotLocale",]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisScope) -> str:
    return value


def deserialize_json(data: str) -> AnalysisScope:
    return cast(AnalysisScope, data)
