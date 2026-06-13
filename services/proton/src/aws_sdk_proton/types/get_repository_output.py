"""Generated from Smithy shape ``com.amazonaws.proton#GetRepositoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.repository


class GetRepositoryOutput(TypedDict):
    repository: "aws_sdk_proton.types.repository.Repository"
    """<p>The repository link's detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositoryOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.repository

    out["repository"] = aws_sdk_proton.types.repository.serialize_aws_json_1_0(
        value["repository"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositoryOutput:
    out: GetRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_proton.types.repository

        out["repository"] = aws_sdk_proton.types.repository.deserialize_aws_json_1_0(
            data["repository"]
        )
    else:
        raise DeserializationError("GetRepositoryOutput.repository required")
    return out
