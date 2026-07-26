"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.commit


class GetCommitOutput(TypedDict, closed=True):
    commit: "capo_codecommit.types.commit.Commit"
    """<p>A commit data type object that contains information about the specified commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommitOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.commit

    out["commit"] = capo_codecommit.types.commit.serialize_aws_json_1_1(value["commit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommitOutput:
    out: GetCommitOutput = {}  # type: ignore[typeddict-item]
    if "commit" in data:
        import capo_codecommit.types.commit

        out["commit"] = capo_codecommit.types.commit.deserialize_aws_json_1_1(
            data["commit"]
        )
    else:
        raise DeserializationError("GetCommitOutput.commit required")
    return out
