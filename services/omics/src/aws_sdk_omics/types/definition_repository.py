"""Generated from Smithy shape ``com.amazonaws.omics#DefinitionRepository``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.connection_arn
    import aws_sdk_omics.types.exclude_file_pattern_list
    import aws_sdk_omics.types.full_repository_id
    import aws_sdk_omics.types.source_reference


class DefinitionRepository(TypedDict):
    connection_arn: "aws_sdk_omics.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection to the source code repository.</p>"""
    full_repository_id: "aws_sdk_omics.types.full_repository_id.FullRepositoryId"
    """<p>The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.</p>"""
    source_reference: NotRequired[
        "aws_sdk_omics.types.source_reference.SourceReference"
    ]
    """<p>The source reference for the repository, such as a branch name, tag, or commit ID.</p>"""
    exclude_file_patterns: NotRequired[
        "aws_sdk_omics.types.exclude_file_pattern_list.ExcludeFilePatternList"
    ]
    """<p>A list of file patterns to exclude when retrieving the workflow definition from the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefinitionRepository) -> dict:
    out: dict = {}
    out["connectionArn"] = value["connection_arn"]
    out["fullRepositoryId"] = value["full_repository_id"]
    if "source_reference" in value:
        import aws_sdk_omics.types.source_reference

        out["sourceReference"] = aws_sdk_omics.types.source_reference.serialize_json(
            value["source_reference"]
        )
    if "exclude_file_patterns" in value:
        import aws_sdk_omics.types.exclude_file_pattern_list

        out["excludeFilePatterns"] = (
            aws_sdk_omics.types.exclude_file_pattern_list.serialize_json(
                value["exclude_file_patterns"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefinitionRepository:
    out: DefinitionRepository = {}  # type: ignore[typeddict-item]
    if "connectionArn" in data:
        out["connection_arn"] = data["connectionArn"]
    else:
        raise DeserializationError("DefinitionRepository.connection_arn required")
    if "fullRepositoryId" in data:
        out["full_repository_id"] = data["fullRepositoryId"]
    else:
        raise DeserializationError("DefinitionRepository.full_repository_id required")
    if "sourceReference" in data:
        import aws_sdk_omics.types.source_reference

        out["source_reference"] = aws_sdk_omics.types.source_reference.deserialize_json(
            data["sourceReference"]
        )
    if "excludeFilePatterns" in data:
        import aws_sdk_omics.types.exclude_file_pattern_list

        out["exclude_file_patterns"] = (
            aws_sdk_omics.types.exclude_file_pattern_list.deserialize_json(
                data["excludeFilePatterns"]
            )
        )
    return out
