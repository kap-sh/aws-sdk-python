"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerativeAISettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.buildtime_settings
    import capo_lex_models_v2.types.runtime_settings


class GenerativeAISettings(TypedDict, closed=True):
    runtime_settings: NotRequired[
        "capo_lex_models_v2.types.runtime_settings.RuntimeSettings"
    ]
    buildtime_settings: NotRequired[
        "capo_lex_models_v2.types.buildtime_settings.BuildtimeSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeAISettings) -> dict:
    out: dict = {}
    if "runtime_settings" in value:
        import capo_lex_models_v2.types.runtime_settings

        out["runtimeSettings"] = (
            capo_lex_models_v2.types.runtime_settings.serialize_json(
                value["runtime_settings"]
            )
        )
    if "buildtime_settings" in value:
        import capo_lex_models_v2.types.buildtime_settings

        out["buildtimeSettings"] = (
            capo_lex_models_v2.types.buildtime_settings.serialize_json(
                value["buildtime_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerativeAISettings:
    out: GenerativeAISettings = {}  # type: ignore[typeddict-item]
    if "runtimeSettings" in data:
        import capo_lex_models_v2.types.runtime_settings

        out["runtime_settings"] = (
            capo_lex_models_v2.types.runtime_settings.deserialize_json(
                data["runtimeSettings"]
            )
        )
    if "buildtimeSettings" in data:
        import capo_lex_models_v2.types.buildtime_settings

        out["buildtime_settings"] = (
            capo_lex_models_v2.types.buildtime_settings.deserialize_json(
                data["buildtimeSettings"]
            )
        )
    return out
