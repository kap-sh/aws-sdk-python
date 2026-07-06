"""Generated from Smithy shape ``com.amazonaws.ssm#ListAssociationVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_version_list
    import aws_sdk_ssm.types.next_token


class ListAssociationVersionsResult(TypedDict, closed=True):
    association_versions: NotRequired[
        "aws_sdk_ssm.types.association_version_list.AssociationVersionList"
    ]
    """<p>Information about all versions of the association for the specified association ID.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociationVersionsResult) -> dict:
    out: dict = {}
    if "association_versions" in value:
        import aws_sdk_ssm.types.association_version_list

        out["AssociationVersions"] = (
            aws_sdk_ssm.types.association_version_list.serialize_aws_json_1_1(
                value["association_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociationVersionsResult:
    out: ListAssociationVersionsResult = {}  # type: ignore[typeddict-item]
    if "AssociationVersions" in data:
        import aws_sdk_ssm.types.association_version_list

        out["association_versions"] = (
            aws_sdk_ssm.types.association_version_list.deserialize_aws_json_1_1(
                data["AssociationVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
