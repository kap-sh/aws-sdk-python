"""Generated from Smithy shape ``com.amazonaws.codecommit#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.reference_name
    import capo_codecommit.types.repository_name


class Target(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the pull request.</p>"""
    source_reference: "capo_codecommit.types.reference_name.ReferenceName"
    """<p>The branch of the repository that contains the changes for the pull request. Also known as the source branch.</p>"""
    destination_reference: NotRequired[
        "capo_codecommit.types.reference_name.ReferenceName"
    ]
    """<p>The branch of the repository where the pull request changes are merged. Also known as the destination branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Target) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["sourceReference"] = value["source_reference"]
    if "destination_reference" in value:
        out["destinationReference"] = value["destination_reference"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("Target.repository_name required")
    if "sourceReference" in data:
        out["source_reference"] = data["sourceReference"]
    else:
        raise DeserializationError("Target.source_reference required")
    if "destinationReference" in data:
        out["destination_reference"] = data["destinationReference"]
    return out
