"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_version_list
    import capo_ssm.types.next_token


class ListDocumentVersionsResult(TypedDict, closed=True):
    document_versions: NotRequired[
        "capo_ssm.types.document_version_list.DocumentVersionList"
    ]
    """<p>The document versions.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentVersionsResult) -> dict:
    out: dict = {}
    if "document_versions" in value:
        import capo_ssm.types.document_version_list

        out["DocumentVersions"] = (
            capo_ssm.types.document_version_list.serialize_aws_json_1_1(
                value["document_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentVersionsResult:
    out: ListDocumentVersionsResult = {}  # type: ignore[typeddict-item]
    if data.get("DocumentVersions") is not None:
        import capo_ssm.types.document_version_list

        out["document_versions"] = (
            capo_ssm.types.document_version_list.deserialize_aws_json_1_1(
                data["DocumentVersions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
