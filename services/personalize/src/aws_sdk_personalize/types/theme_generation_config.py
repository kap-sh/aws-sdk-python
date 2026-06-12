"""Generated from Smithy shape ``com.amazonaws.personalize#ThemeGenerationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.fields_for_theme_generation


class ThemeGenerationConfig(TypedDict):
    fields_for_theme_generation: (
        "aws_sdk_personalize.types.fields_for_theme_generation.FieldsForThemeGeneration"
    )
    """<p>Fields used to generate descriptive themes for a batch inference job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeGenerationConfig) -> dict:
    out: dict = {}
    import aws_sdk_personalize.types.fields_for_theme_generation

    out["fieldsForThemeGeneration"] = (
        aws_sdk_personalize.types.fields_for_theme_generation.serialize_aws_json_1_1(
            value["fields_for_theme_generation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ThemeGenerationConfig:
    out: ThemeGenerationConfig = {}  # type: ignore[typeddict-item]
    if "fieldsForThemeGeneration" in data:
        import aws_sdk_personalize.types.fields_for_theme_generation

        out["fields_for_theme_generation"] = (
            aws_sdk_personalize.types.fields_for_theme_generation.deserialize_aws_json_1_1(
                data["fieldsForThemeGeneration"]
            )
        )
    else:
        raise DeserializationError(
            "ThemeGenerationConfig.fields_for_theme_generation required"
        )
    return out
