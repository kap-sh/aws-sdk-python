"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceAlgorithmSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.source_algorithm_list


class SourceAlgorithmSpecification(TypedDict):
    source_algorithms: NotRequired[
        "aws_sdk_sagemaker.types.source_algorithm_list.SourceAlgorithmList"
    ]
    """<p>A list of the algorithms that were used to create a model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAlgorithmSpecification) -> dict:
    out: dict = {}
    if "source_algorithms" in value:
        import aws_sdk_sagemaker.types.source_algorithm_list

        out["SourceAlgorithms"] = (
            aws_sdk_sagemaker.types.source_algorithm_list.serialize_aws_json_1_1(
                value["source_algorithms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceAlgorithmSpecification:
    out: SourceAlgorithmSpecification = {}  # type: ignore[typeddict-item]
    if "SourceAlgorithms" in data:
        import aws_sdk_sagemaker.types.source_algorithm_list

        out["source_algorithms"] = (
            aws_sdk_sagemaker.types.source_algorithm_list.deserialize_aws_json_1_1(
                data["SourceAlgorithms"]
            )
        )
    return out
