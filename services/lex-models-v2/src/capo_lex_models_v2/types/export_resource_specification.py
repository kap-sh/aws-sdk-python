"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportResourceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_export_specification
    import capo_lex_models_v2.types.bot_locale_export_specification
    import capo_lex_models_v2.types.custom_vocabulary_export_specification
    import capo_lex_models_v2.types.test_set_export_specification


class ExportResourceSpecification(TypedDict, closed=True):
    bot_export_specification: NotRequired[
        "capo_lex_models_v2.types.bot_export_specification.BotExportSpecification"
    ]
    """<p>Parameters for exporting a bot.</p>"""
    bot_locale_export_specification: NotRequired[
        "capo_lex_models_v2.types.bot_locale_export_specification.BotLocaleExportSpecification"
    ]
    """<p>Parameters for exporting a bot locale.</p>"""
    custom_vocabulary_export_specification: NotRequired[
        "capo_lex_models_v2.types.custom_vocabulary_export_specification.CustomVocabularyExportSpecification"
    ]
    """<p>The parameters required to export a custom vocabulary.</p>"""
    test_set_export_specification: NotRequired[
        "capo_lex_models_v2.types.test_set_export_specification.TestSetExportSpecification"
    ]
    """<p>Specifications for the test set that is exported as a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportResourceSpecification) -> dict:
    out: dict = {}
    if "bot_export_specification" in value:
        import capo_lex_models_v2.types.bot_export_specification

        out["botExportSpecification"] = (
            capo_lex_models_v2.types.bot_export_specification.serialize_json(
                value["bot_export_specification"]
            )
        )
    if "bot_locale_export_specification" in value:
        import capo_lex_models_v2.types.bot_locale_export_specification

        out["botLocaleExportSpecification"] = (
            capo_lex_models_v2.types.bot_locale_export_specification.serialize_json(
                value["bot_locale_export_specification"]
            )
        )
    if "custom_vocabulary_export_specification" in value:
        import capo_lex_models_v2.types.custom_vocabulary_export_specification

        out["customVocabularyExportSpecification"] = (
            capo_lex_models_v2.types.custom_vocabulary_export_specification.serialize_json(
                value["custom_vocabulary_export_specification"]
            )
        )
    if "test_set_export_specification" in value:
        import capo_lex_models_v2.types.test_set_export_specification

        out["testSetExportSpecification"] = (
            capo_lex_models_v2.types.test_set_export_specification.serialize_json(
                value["test_set_export_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportResourceSpecification:
    out: ExportResourceSpecification = {}  # type: ignore[typeddict-item]
    if "botExportSpecification" in data:
        import capo_lex_models_v2.types.bot_export_specification

        out["bot_export_specification"] = (
            capo_lex_models_v2.types.bot_export_specification.deserialize_json(
                data["botExportSpecification"]
            )
        )
    if "botLocaleExportSpecification" in data:
        import capo_lex_models_v2.types.bot_locale_export_specification

        out["bot_locale_export_specification"] = (
            capo_lex_models_v2.types.bot_locale_export_specification.deserialize_json(
                data["botLocaleExportSpecification"]
            )
        )
    if "customVocabularyExportSpecification" in data:
        import capo_lex_models_v2.types.custom_vocabulary_export_specification

        out["custom_vocabulary_export_specification"] = (
            capo_lex_models_v2.types.custom_vocabulary_export_specification.deserialize_json(
                data["customVocabularyExportSpecification"]
            )
        )
    if "testSetExportSpecification" in data:
        import capo_lex_models_v2.types.test_set_export_specification

        out["test_set_export_specification"] = (
            capo_lex_models_v2.types.test_set_export_specification.deserialize_json(
                data["testSetExportSpecification"]
            )
        )
    return out
