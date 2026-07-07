"""Generated from Smithy shape ``com.amazonaws.proton#CreateRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.repository


class CreateRepositoryOutput(TypedDict, closed=True):
    repository: "aws_sdk_proton.types.repository.Repository"
    """<p>The repository link's detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRepositoryOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.repository

    out["repository"] = aws_sdk_proton.types.repository.serialize_aws_json_1_0(
        value["repository"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRepositoryOutput:
    out: CreateRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_proton.types.repository

        out["repository"] = aws_sdk_proton.types.repository.deserialize_aws_json_1_0(
            data["repository"]
        )
    else:
        raise DeserializationError("CreateRepositoryOutput.repository required")
    return out
