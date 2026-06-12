"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#QnAIntentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bedrock_model_specification
    import aws_sdk_lex_models_v2.types.data_source_configuration


class QnAIntentConfiguration(TypedDict):
    data_source_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Contains details about the configuration of the data source used for the <code>AMAZON.QnAIntent</code>.</p>"""
    bedrock_model_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_model_specification.BedrockModelSpecification"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: QnAIntentConfiguration) -> dict:
    out: dict = {}
    if "data_source_configuration" in value:
        import aws_sdk_lex_models_v2.types.data_source_configuration

        out["dataSourceConfiguration"] = (
            aws_sdk_lex_models_v2.types.data_source_configuration.serialize_json(
                value["data_source_configuration"]
            )
        )
    if "bedrock_model_configuration" in value:
        import aws_sdk_lex_models_v2.types.bedrock_model_specification

        out["bedrockModelConfiguration"] = (
            aws_sdk_lex_models_v2.types.bedrock_model_specification.serialize_json(
                value["bedrock_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> QnAIntentConfiguration:
    out: QnAIntentConfiguration = {}  # type: ignore[typeddict-item]
    if "dataSourceConfiguration" in data:
        import aws_sdk_lex_models_v2.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_lex_models_v2.types.data_source_configuration.deserialize_json(
                data["dataSourceConfiguration"]
            )
        )
    if "bedrockModelConfiguration" in data:
        import aws_sdk_lex_models_v2.types.bedrock_model_specification

        out["bedrock_model_configuration"] = (
            aws_sdk_lex_models_v2.types.bedrock_model_specification.deserialize_json(
                data["bedrockModelConfiguration"]
            )
        )
    return out
