"""Generated from Smithy shape ``com.amazonaws.support#DescribeSupportedLanguagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.supported_languages_list


class DescribeSupportedLanguagesResponse(TypedDict, closed=True):
    supported_languages: NotRequired[
        "capo_support.types.supported_languages_list.SupportedLanguagesList"
    ]
    """<p> A JSON-formatted array that contains the available ISO 639-1 language codes. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSupportedLanguagesResponse) -> dict:
    out: dict = {}
    if "supported_languages" in value:
        import capo_support.types.supported_languages_list

        out["supportedLanguages"] = (
            capo_support.types.supported_languages_list.serialize_aws_json_1_1(
                value["supported_languages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSupportedLanguagesResponse:
    out: DescribeSupportedLanguagesResponse = {}  # type: ignore[typeddict-item]
    if "supportedLanguages" in data:
        import capo_support.types.supported_languages_list

        out["supported_languages"] = (
            capo_support.types.supported_languages_list.deserialize_aws_json_1_1(
                data["supportedLanguages"]
            )
        )
    return out
