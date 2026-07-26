"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceAlgorithmSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.source_algorithm_list


class SourceAlgorithmSpecification(TypedDict, closed=True):
    source_algorithms: NotRequired[
        "capo_sagemaker.types.source_algorithm_list.SourceAlgorithmList"
    ]
    """<p>A list of the algorithms that were used to create a model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAlgorithmSpecification) -> dict:
    out: dict = {}
    if "source_algorithms" in value:
        import capo_sagemaker.types.source_algorithm_list

        out["SourceAlgorithms"] = (
            capo_sagemaker.types.source_algorithm_list.serialize_aws_json_1_1(
                value["source_algorithms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceAlgorithmSpecification:
    out: SourceAlgorithmSpecification = {}  # type: ignore[typeddict-item]
    if "SourceAlgorithms" in data:
        import capo_sagemaker.types.source_algorithm_list

        out["source_algorithms"] = (
            capo_sagemaker.types.source_algorithm_list.deserialize_aws_json_1_1(
                data["SourceAlgorithms"]
            )
        )
    return out
