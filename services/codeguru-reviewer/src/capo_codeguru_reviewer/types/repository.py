"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Repository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.code_commit_repository
    import capo_codeguru_reviewer.types.s3_repository
    import capo_codeguru_reviewer.types.third_party_source_repository


class Repository(TypedDict, closed=True):
    code_commit: NotRequired[
        "capo_codeguru_reviewer.types.code_commit_repository.CodeCommitRepository"
    ]
    """<p>Information about an Amazon Web Services CodeCommit repository.</p>"""
    bitbucket: NotRequired[
        "capo_codeguru_reviewer.types.third_party_source_repository.ThirdPartySourceRepository"
    ]
    """<p> Information about a Bitbucket repository. </p>"""
    git_hub_enterprise_server: NotRequired[
        "capo_codeguru_reviewer.types.third_party_source_repository.ThirdPartySourceRepository"
    ]
    """<p>Information about a GitHub Enterprise Server repository.</p>"""
    s3_bucket: NotRequired["capo_codeguru_reviewer.types.s3_repository.S3Repository"]


# --- restJson1 ser/de ---
def serialize_json(value: Repository) -> dict:
    out: dict = {}
    if "code_commit" in value:
        import capo_codeguru_reviewer.types.code_commit_repository

        out["CodeCommit"] = (
            capo_codeguru_reviewer.types.code_commit_repository.serialize_json(
                value["code_commit"]
            )
        )
    if "bitbucket" in value:
        import capo_codeguru_reviewer.types.third_party_source_repository

        out["Bitbucket"] = (
            capo_codeguru_reviewer.types.third_party_source_repository.serialize_json(
                value["bitbucket"]
            )
        )
    if "git_hub_enterprise_server" in value:
        import capo_codeguru_reviewer.types.third_party_source_repository

        out["GitHubEnterpriseServer"] = (
            capo_codeguru_reviewer.types.third_party_source_repository.serialize_json(
                value["git_hub_enterprise_server"]
            )
        )
    if "s3_bucket" in value:
        import capo_codeguru_reviewer.types.s3_repository

        out["S3Bucket"] = capo_codeguru_reviewer.types.s3_repository.serialize_json(
            value["s3_bucket"]
        )
    return out


def deserialize_json(data: dict) -> Repository:
    out: Repository = {}  # type: ignore[typeddict-item]
    if "CodeCommit" in data:
        import capo_codeguru_reviewer.types.code_commit_repository

        out["code_commit"] = (
            capo_codeguru_reviewer.types.code_commit_repository.deserialize_json(
                data["CodeCommit"]
            )
        )
    if "Bitbucket" in data:
        import capo_codeguru_reviewer.types.third_party_source_repository

        out["bitbucket"] = (
            capo_codeguru_reviewer.types.third_party_source_repository.deserialize_json(
                data["Bitbucket"]
            )
        )
    if "GitHubEnterpriseServer" in data:
        import capo_codeguru_reviewer.types.third_party_source_repository

        out["git_hub_enterprise_server"] = (
            capo_codeguru_reviewer.types.third_party_source_repository.deserialize_json(
                data["GitHubEnterpriseServer"]
            )
        )
    if "S3Bucket" in data:
        import capo_codeguru_reviewer.types.s3_repository

        out["s3_bucket"] = capo_codeguru_reviewer.types.s3_repository.deserialize_json(
            data["S3Bucket"]
        )
    return out
