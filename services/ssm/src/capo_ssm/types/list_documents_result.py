"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_identifier_list
    import capo_ssm.types.next_token


class ListDocumentsResult(TypedDict, closed=True):
    document_identifiers: NotRequired[
        "capo_ssm.types.document_identifier_list.DocumentIdentifierList"
    ]
    """<p>The names of the SSM documents.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentsResult) -> dict:
    out: dict = {}
    if "document_identifiers" in value:
        import capo_ssm.types.document_identifier_list

        out["DocumentIdentifiers"] = (
            capo_ssm.types.document_identifier_list.serialize_aws_json_1_1(
                value["document_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentsResult:
    out: ListDocumentsResult = {}  # type: ignore[typeddict-item]
    if data.get("DocumentIdentifiers") is not None:
        import capo_ssm.types.document_identifier_list

        out["document_identifiers"] = (
            capo_ssm.types.document_identifier_list.deserialize_aws_json_1_1(
                data["DocumentIdentifiers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
