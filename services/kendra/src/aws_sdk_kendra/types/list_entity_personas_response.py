"""Generated from Smithy shape ``com.amazonaws.kendra#ListEntityPersonasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.next_token
    import aws_sdk_kendra.types.personas_summary_list


class ListEntityPersonasResponse(TypedDict):
    summary_items: NotRequired[
        "aws_sdk_kendra.types.personas_summary_list.PersonasSummaryList"
    ]
    """<p>An array of summary information for one or more users or groups.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token, which you can use in a later request to retrieve the next set of users or groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntityPersonasResponse) -> dict:
    out: dict = {}
    if "summary_items" in value:
        import aws_sdk_kendra.types.personas_summary_list

        out["SummaryItems"] = (
            aws_sdk_kendra.types.personas_summary_list.serialize_aws_json_1_1(
                value["summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntityPersonasResponse:
    out: ListEntityPersonasResponse = {}  # type: ignore[typeddict-item]
    if "SummaryItems" in data:
        import aws_sdk_kendra.types.personas_summary_list

        out["summary_items"] = (
            aws_sdk_kendra.types.personas_summary_list.deserialize_aws_json_1_1(
                data["SummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
