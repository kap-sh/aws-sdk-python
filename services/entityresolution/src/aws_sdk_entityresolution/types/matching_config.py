"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchingConfig``."""

from typing import TypedDict

from typing_extensions import NotRequired


class MatchingConfig(TypedDict):
    enable_transitive_matching: NotRequired["bool"]
    """<p>Enables transitive matching for the rule-based matching workflow. When enabled, records that match through different rules are grouped together into the same match group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingConfig) -> dict:
    out: dict = {}
    if "enable_transitive_matching" in value:
        out["enableTransitiveMatching"] = value["enable_transitive_matching"]
    return out


def deserialize_json(data: dict) -> MatchingConfig:
    out: MatchingConfig = {}  # type: ignore[typeddict-item]
    if "enableTransitiveMatching" in data:
        out["enable_transitive_matching"] = data["enableTransitiveMatching"]
    return out
