"""Generated from Smithy shape ``com.amazonaws.appconfig#AppliedExtensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.applied_extension

AppliedExtensions: TypeAlias = list[
    "capo_appconfig.types.applied_extension.AppliedExtension"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppliedExtensions) -> list:
    import capo_appconfig.types.applied_extension

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.applied_extension.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppliedExtensions:
    import capo_appconfig.types.applied_extension

    out: AppliedExtensions = []
    for item in data:
        out.append(capo_appconfig.types.applied_extension.deserialize_json(item))
    return out
