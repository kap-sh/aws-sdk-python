"""Generated from Smithy shape ``com.amazonaws.elementalinference#OutputConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.clipping_config
    import capo_elementalinference.types.cropping_config
    import capo_elementalinference.types.subtitling_config


class _OutputConfig_cropping(TypedDict, closed=True):
    cropping: "capo_elementalinference.types.cropping_config.CroppingConfig"


class _OutputConfig_clipping(TypedDict, closed=True):
    clipping: "capo_elementalinference.types.clipping_config.ClippingConfig"


class _OutputConfig_subtitling(TypedDict, closed=True):
    subtitling: "capo_elementalinference.types.subtitling_config.SubtitlingConfig"


OutputConfig: TypeAlias = (
    _OutputConfig_cropping | _OutputConfig_clipping | _OutputConfig_subtitling
)


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfig) -> dict:
    if "cropping" in value:
        import capo_elementalinference.types.cropping_config

        return {
            "cropping": capo_elementalinference.types.cropping_config.serialize_json(
                value["cropping"]
            )
        }
    elif "clipping" in value:
        import capo_elementalinference.types.clipping_config

        return {
            "clipping": capo_elementalinference.types.clipping_config.serialize_json(
                value["clipping"]
            )
        }
    elif "subtitling" in value:
        import capo_elementalinference.types.subtitling_config

        return {
            "subtitling": capo_elementalinference.types.subtitling_config.serialize_json(
                value["subtitling"]
            )
        }
    else:
        raise SerializationError("OutputConfig: no variant present")


def deserialize_json(data: dict) -> OutputConfig:
    if "cropping" in data:
        import capo_elementalinference.types.cropping_config

        return {
            "cropping": capo_elementalinference.types.cropping_config.deserialize_json(
                data["cropping"]
            )
        }
    elif "clipping" in data:
        import capo_elementalinference.types.clipping_config

        return {
            "clipping": capo_elementalinference.types.clipping_config.deserialize_json(
                data["clipping"]
            )
        }
    elif "subtitling" in data:
        import capo_elementalinference.types.subtitling_config

        return {
            "subtitling": capo_elementalinference.types.subtitling_config.deserialize_json(
                data["subtitling"]
            )
        }
    else:
        raise DeserializationError("OutputConfig: no recognized variant key")
