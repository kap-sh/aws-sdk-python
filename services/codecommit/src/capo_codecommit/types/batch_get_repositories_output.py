"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetRepositoriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.batch_get_repositories_errors_list
    import capo_codecommit.types.repository_metadata_list
    import capo_codecommit.types.repository_not_found_list


class BatchGetRepositoriesOutput(TypedDict, closed=True):
    repositories: NotRequired[
        "capo_codecommit.types.repository_metadata_list.RepositoryMetadataList"
    ]
    """<p>A list of repositories returned by the batch get repositories operation.</p>"""
    repositories_not_found: NotRequired[
        "capo_codecommit.types.repository_not_found_list.RepositoryNotFoundList"
    ]
    """<p>Returns a list of repository names for which information could not be found.</p>"""
    errors: NotRequired[
        "capo_codecommit.types.batch_get_repositories_errors_list.BatchGetRepositoriesErrorsList"
    ]
    """<p>Returns information about any errors returned when attempting to retrieve information about the repositories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetRepositoriesOutput) -> dict:
    out: dict = {}
    if "repositories" in value:
        import capo_codecommit.types.repository_metadata_list

        out["repositories"] = (
            capo_codecommit.types.repository_metadata_list.serialize_aws_json_1_1(
                value["repositories"]
            )
        )
    if "repositories_not_found" in value:
        import capo_codecommit.types.repository_not_found_list

        out["repositoriesNotFound"] = (
            capo_codecommit.types.repository_not_found_list.serialize_aws_json_1_1(
                value["repositories_not_found"]
            )
        )
    if "errors" in value:
        import capo_codecommit.types.batch_get_repositories_errors_list

        out["errors"] = (
            capo_codecommit.types.batch_get_repositories_errors_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetRepositoriesOutput:
    out: BatchGetRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import capo_codecommit.types.repository_metadata_list

        out["repositories"] = (
            capo_codecommit.types.repository_metadata_list.deserialize_aws_json_1_1(
                data["repositories"]
            )
        )
    if "repositoriesNotFound" in data:
        import capo_codecommit.types.repository_not_found_list

        out["repositories_not_found"] = (
            capo_codecommit.types.repository_not_found_list.deserialize_aws_json_1_1(
                data["repositoriesNotFound"]
            )
        )
    if "errors" in data:
        import capo_codecommit.types.batch_get_repositories_errors_list

        out["errors"] = (
            capo_codecommit.types.batch_get_repositories_errors_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
