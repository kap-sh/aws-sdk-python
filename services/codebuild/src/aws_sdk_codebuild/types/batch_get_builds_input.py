"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetBuildsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_ids


class BatchGetBuildsInput(TypedDict):
    ids: "aws_sdk_codebuild.types.build_ids.BuildIds"
    """<p>The IDs of the builds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBuildsInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.build_ids

    out["ids"] = aws_sdk_codebuild.types.build_ids.serialize_aws_json_1_1(value["ids"])
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBuildsInput:
    out: BatchGetBuildsInput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_codebuild.types.build_ids

        out["ids"] = aws_sdk_codebuild.types.build_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        raise DeserializationError("BatchGetBuildsInput.ids required")
    return out
