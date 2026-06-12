"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#DescribeRepositoryAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.repository_association
    import aws_sdk_codeguru_reviewer.types.tag_map


class DescribeRepositoryAssociationResponse(TypedDict):
    repository_association: NotRequired[
        "aws_sdk_codeguru_reviewer.types.repository_association.RepositoryAssociation"
    ]
    """<p>Information about the repository association.</p>"""
    tags: NotRequired["aws_sdk_codeguru_reviewer.types.tag_map.TagMap"]
    """<p>An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A <i>tag key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag keys are case sensitive.</p> </li> <li> <p>An optional field known as a <i>tag value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRepositoryAssociationResponse) -> dict:
    out: dict = {}
    if "repository_association" in value:
        import aws_sdk_codeguru_reviewer.types.repository_association

        out["RepositoryAssociation"] = (
            aws_sdk_codeguru_reviewer.types.repository_association.serialize_json(
                value["repository_association"]
            )
        )
    if "tags" in value:
        import aws_sdk_codeguru_reviewer.types.tag_map

        out["Tags"] = aws_sdk_codeguru_reviewer.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribeRepositoryAssociationResponse:
    out: DescribeRepositoryAssociationResponse = {}  # type: ignore[typeddict-item]
    if "RepositoryAssociation" in data:
        import aws_sdk_codeguru_reviewer.types.repository_association

        out["repository_association"] = (
            aws_sdk_codeguru_reviewer.types.repository_association.deserialize_json(
                data["RepositoryAssociation"]
            )
        )
    if "Tags" in data:
        import aws_sdk_codeguru_reviewer.types.tag_map

        out["tags"] = aws_sdk_codeguru_reviewer.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
