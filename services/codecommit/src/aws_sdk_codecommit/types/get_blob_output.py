"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBlobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.blob


class GetBlobOutput(TypedDict):
    content: "aws_sdk_codecommit.types.blob.blob"
    """<p>The content of the blob, usually a file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlobOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.blob

    out["content"] = aws_sdk_codecommit.types.blob.serialize_aws_json_1_1(
        value["content"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlobOutput:
    out: GetBlobOutput = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_codecommit.types.blob

        out["content"] = aws_sdk_codecommit.types.blob.deserialize_aws_json_1_1(
            data["content"]
        )
    else:
        raise DeserializationError("GetBlobOutput.content required")
    return out
