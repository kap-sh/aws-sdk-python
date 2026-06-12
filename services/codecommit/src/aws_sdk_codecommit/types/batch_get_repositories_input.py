"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetRepositoriesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_name_list


class BatchGetRepositoriesInput(TypedDict):
    repository_names: "aws_sdk_codecommit.types.repository_name_list.RepositoryNameList"
    """<p>The names of the repositories to get information about.</p> <note> <p>The length constraint limit is for each string in the array. The array itself can be empty.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetRepositoriesInput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.repository_name_list

    out["repositoryNames"] = (
        aws_sdk_codecommit.types.repository_name_list.serialize_aws_json_1_1(
            value["repository_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetRepositoriesInput:
    out: BatchGetRepositoriesInput = {}  # type: ignore[typeddict-item]
    if "repositoryNames" in data:
        import aws_sdk_codecommit.types.repository_name_list

        out["repository_names"] = (
            aws_sdk_codecommit.types.repository_name_list.deserialize_aws_json_1_1(
                data["repositoryNames"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetRepositoriesInput.repository_names required"
        )
    return out
