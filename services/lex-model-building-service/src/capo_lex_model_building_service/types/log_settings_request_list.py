"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#LogSettingsRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.log_settings_request

LogSettingsRequestList: TypeAlias = list[
    "capo_lex_model_building_service.types.log_settings_request.LogSettingsRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogSettingsRequestList) -> list:
    import capo_lex_model_building_service.types.log_settings_request

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.log_settings_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LogSettingsRequestList:
    import capo_lex_model_building_service.types.log_settings_request

    out: LogSettingsRequestList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.log_settings_request.deserialize_json(
                item
            )
        )
    return out
