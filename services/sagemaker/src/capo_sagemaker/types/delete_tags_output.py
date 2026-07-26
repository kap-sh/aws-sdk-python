"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTagsOutput``."""

from typing_extensions import TypedDict


class DeleteTagsOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsOutput:
    out: DeleteTagsOutput = {}  # type: ignore[typeddict-item]
    return out
