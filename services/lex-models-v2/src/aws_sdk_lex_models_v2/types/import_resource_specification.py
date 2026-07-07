"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportResourceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_import_specification
    import aws_sdk_lex_models_v2.types.bot_locale_import_specification
    import aws_sdk_lex_models_v2.types.custom_vocabulary_import_specification
    import aws_sdk_lex_models_v2.types.test_set_import_resource_specification


class ImportResourceSpecification(TypedDict, closed=True):
    bot_import_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_import_specification.BotImportSpecification"
    ]
    """<p>Parameters for importing a bot.</p>"""
    bot_locale_import_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_locale_import_specification.BotLocaleImportSpecification"
    ]
    """<p>Parameters for importing a bot locale.</p>"""
    custom_vocabulary_import_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.custom_vocabulary_import_specification.CustomVocabularyImportSpecification"
    ]
    test_set_import_resource_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_import_resource_specification.TestSetImportResourceSpecification"
    ]
    """<p>Specifications for the test set that is imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportResourceSpecification) -> dict:
    out: dict = {}
    if "bot_import_specification" in value:
        import aws_sdk_lex_models_v2.types.bot_import_specification

        out["botImportSpecification"] = (
            aws_sdk_lex_models_v2.types.bot_import_specification.serialize_json(
                value["bot_import_specification"]
            )
        )
    if "bot_locale_import_specification" in value:
        import aws_sdk_lex_models_v2.types.bot_locale_import_specification

        out["botLocaleImportSpecification"] = (
            aws_sdk_lex_models_v2.types.bot_locale_import_specification.serialize_json(
                value["bot_locale_import_specification"]
            )
        )
    if "custom_vocabulary_import_specification" in value:
        import aws_sdk_lex_models_v2.types.custom_vocabulary_import_specification

        out["customVocabularyImportSpecification"] = (
            aws_sdk_lex_models_v2.types.custom_vocabulary_import_specification.serialize_json(
                value["custom_vocabulary_import_specification"]
            )
        )
    if "test_set_import_resource_specification" in value:
        import aws_sdk_lex_models_v2.types.test_set_import_resource_specification

        out["testSetImportResourceSpecification"] = (
            aws_sdk_lex_models_v2.types.test_set_import_resource_specification.serialize_json(
                value["test_set_import_resource_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportResourceSpecification:
    out: ImportResourceSpecification = {}  # type: ignore[typeddict-item]
    if "botImportSpecification" in data:
        import aws_sdk_lex_models_v2.types.bot_import_specification

        out["bot_import_specification"] = (
            aws_sdk_lex_models_v2.types.bot_import_specification.deserialize_json(
                data["botImportSpecification"]
            )
        )
    if "botLocaleImportSpecification" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_import_specification

        out["bot_locale_import_specification"] = (
            aws_sdk_lex_models_v2.types.bot_locale_import_specification.deserialize_json(
                data["botLocaleImportSpecification"]
            )
        )
    if "customVocabularyImportSpecification" in data:
        import aws_sdk_lex_models_v2.types.custom_vocabulary_import_specification

        out["custom_vocabulary_import_specification"] = (
            aws_sdk_lex_models_v2.types.custom_vocabulary_import_specification.deserialize_json(
                data["customVocabularyImportSpecification"]
            )
        )
    if "testSetImportResourceSpecification" in data:
        import aws_sdk_lex_models_v2.types.test_set_import_resource_specification

        out["test_set_import_resource_specification"] = (
            aws_sdk_lex_models_v2.types.test_set_import_resource_specification.deserialize_json(
                data["testSetImportResourceSpecification"]
            )
        )
    return out
