"""Generated from Smithy shape ``com.amazonaws.appconfig#ApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.application

ApplicationList: TypeAlias = list["capo_appconfig.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationList) -> list:
    import capo_appconfig.types.application

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationList:
    import capo_appconfig.types.application

    out: ApplicationList = []
    for item in data:
        out.append(capo_appconfig.types.application.deserialize_json(item))
    return out
