"""Generated from Smithy shape ``com.amazonaws.opensearch#AIMLOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.natural_language_query_generation_options_output
    import aws_sdk_opensearch.types.s3_vectors_engine
    import aws_sdk_opensearch.types.serverless_vector_acceleration


class AIMLOptionsOutput(TypedDict, closed=True):
    natural_language_query_generation_options: NotRequired[
        "aws_sdk_opensearch.types.natural_language_query_generation_options_output.NaturalLanguageQueryGenerationOptionsOutput"
    ]
    """<p>Container for parameters required for natural language query generation on the specified domain.</p>"""
    s3_vectors_engine: NotRequired[
        "aws_sdk_opensearch.types.s3_vectors_engine.S3VectorsEngine"
    ]
    """<p>Container for parameters representing the state of S3 vectors engine features on the specified domain.</p>"""
    serverless_vector_acceleration: NotRequired[
        "aws_sdk_opensearch.types.serverless_vector_acceleration.ServerlessVectorAcceleration"
    ]
    """<p>The current serverless vector acceleration configuration for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIMLOptionsOutput) -> dict:
    out: dict = {}
    if "natural_language_query_generation_options" in value:
        import aws_sdk_opensearch.types.natural_language_query_generation_options_output

        out["NaturalLanguageQueryGenerationOptions"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_options_output.serialize_json(
                value["natural_language_query_generation_options"]
            )
        )
    if "s3_vectors_engine" in value:
        import aws_sdk_opensearch.types.s3_vectors_engine

        out["S3VectorsEngine"] = (
            aws_sdk_opensearch.types.s3_vectors_engine.serialize_json(
                value["s3_vectors_engine"]
            )
        )
    if "serverless_vector_acceleration" in value:
        import aws_sdk_opensearch.types.serverless_vector_acceleration

        out["ServerlessVectorAcceleration"] = (
            aws_sdk_opensearch.types.serverless_vector_acceleration.serialize_json(
                value["serverless_vector_acceleration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AIMLOptionsOutput:
    out: AIMLOptionsOutput = {}  # type: ignore[typeddict-item]
    if "NaturalLanguageQueryGenerationOptions" in data:
        import aws_sdk_opensearch.types.natural_language_query_generation_options_output

        out["natural_language_query_generation_options"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_options_output.deserialize_json(
                data["NaturalLanguageQueryGenerationOptions"]
            )
        )
    if "S3VectorsEngine" in data:
        import aws_sdk_opensearch.types.s3_vectors_engine

        out["s3_vectors_engine"] = (
            aws_sdk_opensearch.types.s3_vectors_engine.deserialize_json(
                data["S3VectorsEngine"]
            )
        )
    if "ServerlessVectorAcceleration" in data:
        import aws_sdk_opensearch.types.serverless_vector_acceleration

        out["serverless_vector_acceleration"] = (
            aws_sdk_opensearch.types.serverless_vector_acceleration.deserialize_json(
                data["ServerlessVectorAcceleration"]
            )
        )
    return out
