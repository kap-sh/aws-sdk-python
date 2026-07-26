"""Generated from Smithy shape ``com.amazonaws.polly#Voice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.engine_list
    import capo_polly.types.gender
    import capo_polly.types.language_code
    import capo_polly.types.language_code_list
    import capo_polly.types.language_name
    import capo_polly.types.voice_id
    import capo_polly.types.voice_name


class Voice(TypedDict, closed=True):
    gender: NotRequired["capo_polly.types.gender.Gender"]
    """<p>Gender of the voice.</p>"""
    id: NotRequired["capo_polly.types.voice_id.VoiceId"]
    """<p>Amazon Polly assigned voice ID. This is the ID that you specify when calling the <code>SynthesizeSpeech</code> operation.</p>"""
    language_code: NotRequired["capo_polly.types.language_code.LanguageCode"]
    """<p>Language code of the voice.</p>"""
    language_name: NotRequired["capo_polly.types.language_name.LanguageName"]
    """<p>Human readable name of the language in English.</p>"""
    name: NotRequired["capo_polly.types.voice_name.VoiceName"]
    """<p>Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable voice name that you might display in your application.</p>"""
    additional_language_codes: NotRequired[
        "capo_polly.types.language_code_list.LanguageCodeList"
    ]
    """<p>Additional codes for languages available for the specified voice in addition to its default language. </p> <p>For example, the default language for Aditi is Indian English (en-IN) because it was first used for that language. Since Aditi is bilingual and fluent in both Indian English and Hindi, this parameter would show the code <code>hi-IN</code>.</p>"""
    supported_engines: NotRequired["capo_polly.types.engine_list.EngineList"]
    """<p>Specifies which engines (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) are supported by a given voice.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Voice) -> dict:
    out: dict = {}
    if "gender" in value:
        import capo_polly.types.gender

        out["Gender"] = capo_polly.types.gender.serialize_json(value["gender"])
    if "id" in value:
        import capo_polly.types.voice_id

        out["Id"] = capo_polly.types.voice_id.serialize_json(value["id"])
    if "language_code" in value:
        import capo_polly.types.language_code

        out["LanguageCode"] = capo_polly.types.language_code.serialize_json(
            value["language_code"]
        )
    if "language_name" in value:
        out["LanguageName"] = value["language_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "additional_language_codes" in value:
        import capo_polly.types.language_code_list

        out["AdditionalLanguageCodes"] = (
            capo_polly.types.language_code_list.serialize_json(
                value["additional_language_codes"]
            )
        )
    if "supported_engines" in value:
        import capo_polly.types.engine_list

        out["SupportedEngines"] = capo_polly.types.engine_list.serialize_json(
            value["supported_engines"]
        )
    return out


def deserialize_json(data: dict) -> Voice:
    out: Voice = {}  # type: ignore[typeddict-item]
    if "Gender" in data:
        import capo_polly.types.gender

        out["gender"] = capo_polly.types.gender.deserialize_json(data["Gender"])
    if "Id" in data:
        import capo_polly.types.voice_id

        out["id"] = capo_polly.types.voice_id.deserialize_json(data["Id"])
    if "LanguageCode" in data:
        import capo_polly.types.language_code

        out["language_code"] = capo_polly.types.language_code.deserialize_json(
            data["LanguageCode"]
        )
    if "LanguageName" in data:
        out["language_name"] = data["LanguageName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "AdditionalLanguageCodes" in data:
        import capo_polly.types.language_code_list

        out["additional_language_codes"] = (
            capo_polly.types.language_code_list.deserialize_json(
                data["AdditionalLanguageCodes"]
            )
        )
    if "SupportedEngines" in data:
        import capo_polly.types.engine_list

        out["supported_engines"] = capo_polly.types.engine_list.deserialize_json(
            data["SupportedEngines"]
        )
    return out
