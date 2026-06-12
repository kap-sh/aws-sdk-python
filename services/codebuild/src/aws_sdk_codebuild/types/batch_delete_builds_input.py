"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchDeleteBuildsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_ids


class BatchDeleteBuildsInput(TypedDict):
    ids: "aws_sdk_codebuild.types.build_ids.BuildIds"
    """<p>The IDs of the builds to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteBuildsInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.build_ids

    out["ids"] = aws_sdk_codebuild.types.build_ids.serialize_aws_json_1_1(value["ids"])
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteBuildsInput:
    out: BatchDeleteBuildsInput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.build_ids

        out["ids"] = aws_sdk_codebuild.types.build_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        raise DeserializationError("BatchDeleteBuildsInput.ids required")
    return out
