"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UrlPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.url_pattern

UrlPatternList: TypeAlias = list["capo_workspaces_web.types.url_pattern.UrlPattern"]


# --- restJson1 ser/de ---
def serialize_json(value: UrlPatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> UrlPatternList:
    return list(data)
