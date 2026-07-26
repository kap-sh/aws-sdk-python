"""Generated from Smithy shape ``com.amazonaws.workspacesweb#LocalizedBrandingStringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.locale
    import capo_workspaces_web.types.localized_branding_strings

LocalizedBrandingStringMap: TypeAlias = dict[
    "capo_workspaces_web.types.locale.Locale",
    "capo_workspaces_web.types.localized_branding_strings.LocalizedBrandingStrings",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LocalizedBrandingStringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_workspaces_web.types.locale
        import capo_workspaces_web.types.localized_branding_strings

        out[capo_workspaces_web.types.locale.serialize_json(key)] = (
            capo_workspaces_web.types.localized_branding_strings.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> LocalizedBrandingStringMap:
    out: LocalizedBrandingStringMap = {}
    for key, value in data.items():
        import capo_workspaces_web.types.locale
        import capo_workspaces_web.types.localized_branding_strings

        out[capo_workspaces_web.types.locale.deserialize_json(key)] = (
            capo_workspaces_web.types.localized_branding_strings.deserialize_json(value)
        )
    return out
