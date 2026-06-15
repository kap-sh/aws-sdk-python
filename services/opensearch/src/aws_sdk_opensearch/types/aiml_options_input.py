"""Generated from Smithy shape ``com.amazonaws.opensearch#AIMLOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.natural_language_query_generation_options_input
    import aws_sdk_opensearch.types.s3_vectors_engine
    import aws_sdk_opensearch.types.serverless_vector_acceleration


class AIMLOptionsInput(TypedDict):
    natural_language_query_generation_options: NotRequired[
        "aws_sdk_opensearch.types.natural_language_query_generation_options_input.NaturalLanguageQueryGenerationOptionsInput"
    ]
    """<p>Container for parameters required for natural language query generation on the specified domain.</p>"""
    s3_vectors_engine: NotRequired[
        "aws_sdk_opensearch.types.s3_vectors_engine.S3VectorsEngine"
    ]
    """<p>Container for parameters required to enable S3 vectors engine features on the specified domain.</p>"""
    serverless_vector_acceleration: NotRequired[
        "aws_sdk_opensearch.types.serverless_vector_acceleration.ServerlessVectorAcceleration"
    ]
    r"""<p>Specifies whether to enable serverless vector acceleration for the domain. When enabled, provides <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-vector-index.html\">GPU-accelerated</a> vector search capabilities for improved performance on vector workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIMLOptionsInput) -> dict:
    out: dict = {}
    if "natural_language_query_generation_options" in value:
        import aws_sdk_opensearch.types.natural_language_query_generation_options_input

        out["NaturalLanguageQueryGenerationOptions"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_options_input.serialize_json(
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


def deserialize_json(data: dict) -> AIMLOptionsInput:
    out: AIMLOptionsInput = {}  # type: ignore[typeddict-item]
    if "NaturalLanguageQueryGenerationOptions" in data:
        import aws_sdk_opensearch.types.natural_language_query_generation_options_input

        out["natural_language_query_generation_options"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_options_input.deserialize_json(
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
