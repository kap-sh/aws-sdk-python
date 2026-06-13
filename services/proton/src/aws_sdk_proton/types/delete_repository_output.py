"""Generated from Smithy shape ``com.amazonaws.proton#DeleteRepositoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.repository


class DeleteRepositoryOutput(TypedDict):
    repository: NotRequired["aws_sdk_proton.types.repository.Repository"]
    """<p>The deleted repository link's detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRepositoryOutput) -> dict:
    out: dict = {}
    if "repository" in value:
        import aws_sdk_proton.types.repository

        out["repository"] = aws_sdk_proton.types.repository.serialize_aws_json_1_0(
            value["repository"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRepositoryOutput:
    out: DeleteRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_proton.types.repository

        out["repository"] = aws_sdk_proton.types.repository.deserialize_aws_json_1_0(
            data["repository"]
        )
    return out
