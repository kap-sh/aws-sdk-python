"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#LogSettingsResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.log_settings_response

LogSettingsResponseList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.log_settings_response.LogSettingsResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogSettingsResponseList) -> list:
    import aws_sdk_lex_model_building_service.types.log_settings_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.log_settings_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LogSettingsResponseList:
    import aws_sdk_lex_model_building_service.types.log_settings_response

    out: LogSettingsResponseList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.log_settings_response.deserialize_json(
                item
            )
        )
    return out
