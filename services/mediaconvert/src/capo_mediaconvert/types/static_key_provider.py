"""Generated from Smithy shape ``com.amazonaws.mediaconvert#StaticKeyProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_pattern_a_za_z0932
    import capo_mediaconvert.types.__string_pattern_dd
    import capo_mediaconvert.types.__string_pattern_identity_a_za_z26_a_za_z09163


class StaticKeyProvider(TypedDict, closed=True):
    key_format: NotRequired[
        "capo_mediaconvert.types.__string_pattern_identity_a_za_z26_a_za_z09163.__stringPatternIdentityAZaZ26AZaZ09163"
    ]
    """Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be 'identity' or a reverse DNS string. May be omitted to indicate an implicit value of 'identity'."""
    key_format_versions: NotRequired[
        "capo_mediaconvert.types.__string_pattern_dd.__stringPatternDD"
    ]
    """Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3)."""
    static_key_value: NotRequired[
        "capo_mediaconvert.types.__string_pattern_a_za_z0932.__stringPatternAZaZ0932"
    ]
    """Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value."""
    url: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Relates to DRM implementation. The location of the license server used for protecting content."""


# --- restJson1 ser/de ---
def serialize_json(value: StaticKeyProvider) -> dict:
    out: dict = {}
    if "key_format" in value:
        out["keyFormat"] = value["key_format"]
    if "key_format_versions" in value:
        out["keyFormatVersions"] = value["key_format_versions"]
    if "static_key_value" in value:
        out["staticKeyValue"] = value["static_key_value"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> StaticKeyProvider:
    out: StaticKeyProvider = {}  # type: ignore[typeddict-item]
    if "keyFormat" in data:
        out["key_format"] = data["keyFormat"]
    if "keyFormatVersions" in data:
        out["key_format_versions"] = data["keyFormatVersions"]
    if "staticKeyValue" in data:
        out["static_key_value"] = data["staticKeyValue"]
    if "url" in data:
        out["url"] = data["url"]
    return out
