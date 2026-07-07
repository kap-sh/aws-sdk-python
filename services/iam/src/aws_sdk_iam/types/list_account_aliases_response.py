"""Generated from Smithy shape ``com.amazonaws.iam#ListAccountAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.account_alias_list_type
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.response_marker_type


class ListAccountAliasesResponse(TypedDict, closed=True):
    account_aliases: "aws_sdk_iam.types.account_alias_list_type.accountAliasListType"
    """<p>A list of aliases associated with the account. Amazon Web Services supports only one alias per account.</p>"""
    is_truncated: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["aws_sdk_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAccountAliasesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.account_alias_list_type

    aws_sdk_iam.types.account_alias_list_type.serialize_query(
        value["account_aliases"], pairs, f"{prefix}.AccountAliases"
    )
    pairs.append(
        (
            f"{prefix}.IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListAccountAliasesResponse:
    out: ListAccountAliasesResponse = {}  # type: ignore[typeddict-item]
    child_account_aliases = el.find("AccountAliases")
    if child_account_aliases is not None:
        import aws_sdk_iam.types.account_alias_list_type

        out["account_aliases"] = (
            aws_sdk_iam.types.account_alias_list_type.deserialize_query(
                child_account_aliases
            )
        )
    else:
        raise DeserializationError(
            "ListAccountAliasesResponse.account_aliases required"
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
