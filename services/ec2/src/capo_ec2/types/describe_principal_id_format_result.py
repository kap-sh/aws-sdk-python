"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePrincipalIdFormatResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.principal_id_format_list
    import capo_ec2.types.string


class DescribePrincipalIdFormatResult(TypedDict, closed=True):
    principals: NotRequired[
        "capo_ec2.types.principal_id_format_list.PrincipalIdFormatList"
    ]
    """<p>Information about the ID format settings for the ARN.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePrincipalIdFormatResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "principals" in value:
        import capo_ec2.types.principal_id_format_list

        capo_ec2.types.principal_id_format_list.serialize_ec2_query(
            value["principals"], pairs, f"{key_prefix}PrincipalSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribePrincipalIdFormatResult:
    out: DescribePrincipalIdFormatResult = {}  # type: ignore[typeddict-item]
    child_principals = el.find("principalSet")
    if child_principals is not None:
        import capo_ec2.types.principal_id_format_list

        out["principals"] = (
            capo_ec2.types.principal_id_format_list.deserialize_ec2_query(
                child_principals
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
