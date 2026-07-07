"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormLanguageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_language_code


class EvaluationFormLanguageConfiguration(TypedDict, closed=True):
    form_language: NotRequired[
        "aws_sdk_connect.types.evaluation_form_language_code.EvaluationFormLanguageCode"
    ]
    """<p>The language for the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormLanguageConfiguration) -> dict:
    out: dict = {}
    if "form_language" in value:
        import aws_sdk_connect.types.evaluation_form_language_code

        out["FormLanguage"] = (
            aws_sdk_connect.types.evaluation_form_language_code.serialize_json(
                value["form_language"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormLanguageConfiguration:
    out: EvaluationFormLanguageConfiguration = {}  # type: ignore[typeddict-item]
    if "FormLanguage" in data:
        import aws_sdk_connect.types.evaluation_form_language_code

        out["form_language"] = (
            aws_sdk_connect.types.evaluation_form_language_code.deserialize_json(
                data["FormLanguage"]
            )
        )
    return out
