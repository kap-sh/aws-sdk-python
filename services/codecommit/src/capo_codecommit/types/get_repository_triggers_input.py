"""Generated from Smithy shape ``com.amazonaws.codecommit#GetRepositoryTriggersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.repository_name


class GetRepositoryTriggersInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository for which the trigger is configured.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRepositoryTriggersInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRepositoryTriggersInput:
    out: GetRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "GetRepositoryTriggersInput.repository_name required"
        )
    return out
