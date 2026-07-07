"""Generated from Smithy shape ``com.amazonaws.macie2#ListResourceProfileArtifactsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_resource_profile_artifact
    import aws_sdk_macie2.types.__string


class ListResourceProfileArtifactsResponse(TypedDict, closed=True):
    artifacts: NotRequired[
        "aws_sdk_macie2.types.__list_of_resource_profile_artifact.__listOfResourceProfileArtifact"
    ]
    """<p>An array of objects, one for each of 1-100 S3 objects that Amazon Macie selected for analysis.</p> <p>If Macie has analyzed more than 100 objects in the bucket, Macie populates the array based on the value for the ResourceProfileArtifact.sensitive field for an object: true (sensitive), followed by false (not sensitive). Macie then populates any remaining items in the array with information about objects where the value for the ResourceProfileArtifact.classificationResultStatus field is SKIPPED.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceProfileArtifactsResponse) -> dict:
    out: dict = {}
    if "artifacts" in value:
        import aws_sdk_macie2.types.__list_of_resource_profile_artifact

        out["artifacts"] = (
            aws_sdk_macie2.types.__list_of_resource_profile_artifact.serialize_json(
                value["artifacts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceProfileArtifactsResponse:
    out: ListResourceProfileArtifactsResponse = {}  # type: ignore[typeddict-item]
    if "artifacts" in data:
        import aws_sdk_macie2.types.__list_of_resource_profile_artifact

        out["artifacts"] = (
            aws_sdk_macie2.types.__list_of_resource_profile_artifact.deserialize_json(
                data["artifacts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
