"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KeywordMatchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.boolean
    import capo_chime_sdk_media_pipelines.types.keyword_match_word_list
    import capo_chime_sdk_media_pipelines.types.rule_name


class KeywordMatchConfiguration(TypedDict, closed=True):
    rule_name: "capo_chime_sdk_media_pipelines.types.rule_name.RuleName"
    """<p>The name of the keyword match rule.</p>"""
    keywords: "capo_chime_sdk_media_pipelines.types.keyword_match_word_list.KeywordMatchWordList"
    """<p>The keywords or phrases that you want to match.</p>"""
    negate: "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>Matches keywords or phrases on their presence or absence. If set to <code>TRUE</code>, the rule matches when all the specified keywords or phrases are absent. Default: <code>FALSE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeywordMatchConfiguration) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    import capo_chime_sdk_media_pipelines.types.keyword_match_word_list

    out["Keywords"] = (
        capo_chime_sdk_media_pipelines.types.keyword_match_word_list.serialize_json(
            value["keywords"]
        )
    )
    out["Negate"] = value.get("negate", False)
    return out


def deserialize_json(data: dict) -> KeywordMatchConfiguration:
    out: KeywordMatchConfiguration = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("KeywordMatchConfiguration.rule_name required")
    if "Keywords" in data:
        import capo_chime_sdk_media_pipelines.types.keyword_match_word_list

        out["keywords"] = (
            capo_chime_sdk_media_pipelines.types.keyword_match_word_list.deserialize_json(
                data["Keywords"]
            )
        )
    else:
        raise DeserializationError("KeywordMatchConfiguration.keywords required")
    if "Negate" in data:
        out["negate"] = data["Negate"]
    else:
        out["negate"] = False
    return out
