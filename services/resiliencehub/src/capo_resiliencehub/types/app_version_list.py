"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_version_summary

AppVersionList: TypeAlias = list[
    "capo_resiliencehub.types.app_version_summary.AppVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppVersionList) -> list:
    import capo_resiliencehub.types.app_version_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.app_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppVersionList:
    import capo_resiliencehub.types.app_version_summary

    out: AppVersionList = []
    for item in data:
        out.append(capo_resiliencehub.types.app_version_summary.deserialize_json(item))
    return out
