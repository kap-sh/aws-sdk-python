"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProblemTypeResolvedAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.tabular_resolved_attributes
    import aws_sdk_sagemaker.types.text_generation_resolved_attributes


class _AutoMLProblemTypeResolvedAttributes_TabularResolvedAttributes(
    TypedDict, closed=True
):
    TabularResolvedAttributes: (
        "aws_sdk_sagemaker.types.tabular_resolved_attributes.TabularResolvedAttributes"
    )


class _AutoMLProblemTypeResolvedAttributes_TextGenerationResolvedAttributes(
    TypedDict, closed=True
):
    TextGenerationResolvedAttributes: "aws_sdk_sagemaker.types.text_generation_resolved_attributes.TextGenerationResolvedAttributes"


AutoMLProblemTypeResolvedAttributes: TypeAlias = (
    _AutoMLProblemTypeResolvedAttributes_TabularResolvedAttributes
    | _AutoMLProblemTypeResolvedAttributes_TextGenerationResolvedAttributes
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLProblemTypeResolvedAttributes) -> dict:
    if "TabularResolvedAttributes" in value:
        import aws_sdk_sagemaker.types.tabular_resolved_attributes

        return {
            "TabularResolvedAttributes": aws_sdk_sagemaker.types.tabular_resolved_attributes.serialize_aws_json_1_1(
                value["TabularResolvedAttributes"]
            )
        }
    elif "TextGenerationResolvedAttributes" in value:
        import aws_sdk_sagemaker.types.text_generation_resolved_attributes

        return {
            "TextGenerationResolvedAttributes": aws_sdk_sagemaker.types.text_generation_resolved_attributes.serialize_aws_json_1_1(
                value["TextGenerationResolvedAttributes"]
            )
        }
    else:
        raise SerializationError(
            "AutoMLProblemTypeResolvedAttributes: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> AutoMLProblemTypeResolvedAttributes:
    if "TabularResolvedAttributes" in data:
        import aws_sdk_sagemaker.types.tabular_resolved_attributes

        return {
            "TabularResolvedAttributes": aws_sdk_sagemaker.types.tabular_resolved_attributes.deserialize_aws_json_1_1(
                data["TabularResolvedAttributes"]
            )
        }
    elif "TextGenerationResolvedAttributes" in data:
        import aws_sdk_sagemaker.types.text_generation_resolved_attributes

        return {
            "TextGenerationResolvedAttributes": aws_sdk_sagemaker.types.text_generation_resolved_attributes.deserialize_aws_json_1_1(
                data["TextGenerationResolvedAttributes"]
            )
        }
    else:
        raise DeserializationError(
            "AutoMLProblemTypeResolvedAttributes: no recognized variant key"
        )
