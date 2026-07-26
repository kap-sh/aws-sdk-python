"""Generated from Smithy shape ``com.amazonaws.geoplaces#StreetComponents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.type_placement
    import capo_geo_places.types.type_separator


class StreetComponents(TypedDict, closed=True):
    base_name: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    r"""<p>Base name part of the street name. </p> <p>Example: Younge from the \"Younge street\".</p>"""
    type: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    r"""<p>Street type part of the street name. </p> <p>Example: <code>\"avenue\"</code>.</p>"""
    type_placement: NotRequired["capo_geo_places.types.type_placement.TypePlacement"]
    """<p>Defines if the street type is before or after the base name.</p>"""
    type_separator: NotRequired["capo_geo_places.types.type_separator.TypeSeparator"]
    r"""<p>Defines a separator character such as <code>\"\"</code> or <code>\" \"</code> between the base name and type.</p>"""
    prefix: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>A prefix is a directional identifier that precedes, but is not included in, the base name of a road. </p> <p>Example: E for East.</p>"""
    suffix: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>A suffix is a directional identifier that follows, but is not included in, the base name of a road. </p> <p>Example W for West.</p>"""
    direction: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Indicates the official directional identifiers assigned to highways.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    r"""<p>A <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreetComponents) -> dict:
    out: dict = {}
    if "base_name" in value:
        out["BaseName"] = value["base_name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "type_placement" in value:
        out["TypePlacement"] = value["type_placement"]
    if "type_separator" in value:
        out["TypeSeparator"] = value["type_separator"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    if "direction" in value:
        out["Direction"] = value["direction"]
    if "language" in value:
        out["Language"] = value["language"]
    return out


def deserialize_json(data: dict) -> StreetComponents:
    out: StreetComponents = {}  # type: ignore[typeddict-item]
    if "BaseName" in data:
        out["base_name"] = data["BaseName"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "TypePlacement" in data:
        out["type_placement"] = data["TypePlacement"]
    if "TypeSeparator" in data:
        out["type_separator"] = data["TypeSeparator"]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Suffix" in data:
        out["suffix"] = data["Suffix"]
    if "Direction" in data:
        out["direction"] = data["Direction"]
    if "Language" in data:
        out["language"] = data["Language"]
    return out
