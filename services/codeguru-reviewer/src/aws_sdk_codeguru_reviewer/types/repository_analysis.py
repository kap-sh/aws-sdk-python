"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAnalysis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.repository_head_source_code_type
    import aws_sdk_codeguru_reviewer.types.source_code_type


class RepositoryAnalysis(TypedDict):
    repository_head: NotRequired[
        "aws_sdk_codeguru_reviewer.types.repository_head_source_code_type.RepositoryHeadSourceCodeType"
    ]
    """<p>A <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType\">SourceCodeType</a> that specifies the tip of a branch in an associated repository.</p>"""
    source_code_type: NotRequired[
        "aws_sdk_codeguru_reviewer.types.source_code_type.SourceCodeType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAnalysis) -> dict:
    out: dict = {}
    if "repository_head" in value:
        import aws_sdk_codeguru_reviewer.types.repository_head_source_code_type

        out["RepositoryHead"] = (
            aws_sdk_codeguru_reviewer.types.repository_head_source_code_type.serialize_json(
                value["repository_head"]
            )
        )
    if "source_code_type" in value:
        import aws_sdk_codeguru_reviewer.types.source_code_type

        out["SourceCodeType"] = (
            aws_sdk_codeguru_reviewer.types.source_code_type.serialize_json(
                value["source_code_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> RepositoryAnalysis:
    out: RepositoryAnalysis = {}  # type: ignore[typeddict-item]
    if "RepositoryHead" in data:
        import aws_sdk_codeguru_reviewer.types.repository_head_source_code_type

        out["repository_head"] = (
            aws_sdk_codeguru_reviewer.types.repository_head_source_code_type.deserialize_json(
                data["RepositoryHead"]
            )
        )
    if "SourceCodeType" in data:
        import aws_sdk_codeguru_reviewer.types.source_code_type

        out["source_code_type"] = (
            aws_sdk_codeguru_reviewer.types.source_code_type.deserialize_json(
                data["SourceCodeType"]
            )
        )
    return out
