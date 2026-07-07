"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ObfuscationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.obfuscation_setting_type


class ObfuscationSetting(TypedDict, closed=True):
    obfuscation_setting_type: (
        "aws_sdk_lex_models_v2.types.obfuscation_setting_type.ObfuscationSettingType"
    )
    """<p>Value that determines whether Amazon Lex obscures slot values in conversation logs. The default is to obscure the values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObfuscationSetting) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.obfuscation_setting_type

    out["obfuscationSettingType"] = (
        aws_sdk_lex_models_v2.types.obfuscation_setting_type.serialize_json(
            value["obfuscation_setting_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ObfuscationSetting:
    out: ObfuscationSetting = {}  # type: ignore[typeddict-item]
    if "obfuscationSettingType" in data:
        import aws_sdk_lex_models_v2.types.obfuscation_setting_type

        out["obfuscation_setting_type"] = (
            aws_sdk_lex_models_v2.types.obfuscation_setting_type.deserialize_json(
                data["obfuscationSettingType"]
            )
        )
    else:
        raise DeserializationError(
            "ObfuscationSetting.obfuscation_setting_type required"
        )
    return out
