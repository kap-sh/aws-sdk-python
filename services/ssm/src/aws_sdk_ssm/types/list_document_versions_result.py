"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_version_list
    import aws_sdk_ssm.types.next_token


class ListDocumentVersionsResult(TypedDict, closed=True):
    document_versions: NotRequired[
        "aws_sdk_ssm.types.document_version_list.DocumentVersionList"
    ]
    """<p>The document versions.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentVersionsResult) -> dict:
    out: dict = {}
    if "document_versions" in value:
        import aws_sdk_ssm.types.document_version_list

        out["DocumentVersions"] = (
            aws_sdk_ssm.types.document_version_list.serialize_aws_json_1_1(
                value["document_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentVersionsResult:
    out: ListDocumentVersionsResult = {}  # type: ignore[typeddict-item]
    if "DocumentVersions" in data:
        import aws_sdk_ssm.types.document_version_list

        out["document_versions"] = (
            aws_sdk_ssm.types.document_version_list.deserialize_aws_json_1_1(
                data["DocumentVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
