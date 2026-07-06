"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit


class GetCommitOutput(TypedDict, closed=True):
    commit: "aws_sdk_codecommit.types.commit.Commit"
    """<p>A commit data type object that contains information about the specified commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommitOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.commit

    out["commit"] = aws_sdk_codecommit.types.commit.serialize_aws_json_1_1(
        value["commit"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommitOutput:
    out: GetCommitOutput = {}  # type: ignore[typeddict-item]
    if "commit" in data:
        import aws_sdk_codecommit.types.commit

        out["commit"] = aws_sdk_codecommit.types.commit.deserialize_aws_json_1_1(
            data["commit"]
        )
    else:
        raise DeserializationError("GetCommitOutput.commit required")
    return out
