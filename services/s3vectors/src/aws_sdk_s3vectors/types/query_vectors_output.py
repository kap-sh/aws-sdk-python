"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryVectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.distance_metric
    import aws_sdk_s3vectors.types.query_vectors_output_list


class QueryVectorsOutput(TypedDict, closed=True):
    vectors: "aws_sdk_s3vectors.types.query_vectors_output_list.QueryVectorsOutputList"
    """<p>The vectors in the approximate nearest neighbor search.</p>"""
    distance_metric: NotRequired[
        "aws_sdk_s3vectors.types.distance_metric.DistanceMetric"
    ]
    """<p>The distance metric that was used for the similarity search calculation. This is the same distance metric that was configured for the vector index when it was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryVectorsOutput) -> dict:
    out: dict = {}
    import aws_sdk_s3vectors.types.query_vectors_output_list

    out["vectors"] = aws_sdk_s3vectors.types.query_vectors_output_list.serialize_json(
        value["vectors"]
    )
    if "distance_metric" in value:
        import aws_sdk_s3vectors.types.distance_metric

        out["distanceMetric"] = aws_sdk_s3vectors.types.distance_metric.serialize_json(
            value["distance_metric"]
        )
    return out


def deserialize_json(data: dict) -> QueryVectorsOutput:
    out: QueryVectorsOutput = {}  # type: ignore[typeddict-item]
    if "vectors" in data:
        import aws_sdk_s3vectors.types.query_vectors_output_list

        out["vectors"] = (
            aws_sdk_s3vectors.types.query_vectors_output_list.deserialize_json(
                data["vectors"]
            )
        )
    else:
        raise DeserializationError("QueryVectorsOutput.vectors required")
    if "distanceMetric" in data:
        import aws_sdk_s3vectors.types.distance_metric

        out["distance_metric"] = (
            aws_sdk_s3vectors.types.distance_metric.deserialize_json(
                data["distanceMetric"]
            )
        )
    return out
