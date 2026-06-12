"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_identifier_list
    import aws_sdk_ssm.types.next_token


class ListDocumentsResult(TypedDict):
    document_identifiers: NotRequired[
        "aws_sdk_ssm.types.document_identifier_list.DocumentIdentifierList"
    ]
    """<p>The names of the SSM documents.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentsResult) -> dict:
    out: dict = {}
    if "document_identifiers" in value:
        import aws_sdk_ssm.types.document_identifier_list

        out["DocumentIdentifiers"] = (
            aws_sdk_ssm.types.document_identifier_list.serialize_aws_json_1_1(
                value["document_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentsResult:
    out: ListDocumentsResult = {}  # type: ignore[typeddict-item]
    if "DocumentIdentifiers" in data:
        import aws_sdk_ssm.types.document_identifier_list

        out["document_identifiers"] = (
            aws_sdk_ssm.types.document_identifier_list.deserialize_aws_json_1_1(
                data["DocumentIdentifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
