"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetBuildBatchesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_batch_ids


class BatchGetBuildBatchesInput(TypedDict):
    ids: "aws_sdk_codebuild.types.build_batch_ids.BuildBatchIds"
    """<p>An array that contains the batch build identifiers to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBuildBatchesInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.build_batch_ids

    out["ids"] = aws_sdk_codebuild.types.build_batch_ids.serialize_aws_json_1_1(
        value["ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBuildBatchesInput:
    out: BatchGetBuildBatchesInput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.build_batch_ids

        out["ids"] = aws_sdk_codebuild.types.build_batch_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        raise DeserializationError("BatchGetBuildBatchesInput.ids required")
    return out
