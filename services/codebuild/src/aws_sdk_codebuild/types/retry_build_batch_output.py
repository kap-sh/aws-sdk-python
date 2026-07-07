"""Generated from Smithy shape ``com.amazonaws.codebuild#RetryBuildBatchOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_batch


class RetryBuildBatchOutput(TypedDict, closed=True):
    build_batch: NotRequired["aws_sdk_codebuild.types.build_batch.BuildBatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryBuildBatchOutput) -> dict:
    out: dict = {}
    if "build_batch" in value:
        import aws_sdk_codebuild.types.build_batch

        out["buildBatch"] = aws_sdk_codebuild.types.build_batch.serialize_aws_json_1_1(
            value["build_batch"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryBuildBatchOutput:
    out: RetryBuildBatchOutput = {}  # type: ignore[typeddict-item]
    if "buildBatch" in data:
        import aws_sdk_codebuild.types.build_batch

        out["build_batch"] = (
            aws_sdk_codebuild.types.build_batch.deserialize_aws_json_1_1(
                data["buildBatch"]
            )
        )
    return out
