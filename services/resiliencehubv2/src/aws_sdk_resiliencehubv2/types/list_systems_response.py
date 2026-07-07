"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListSystemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.system_summary_list


class ListSystemsResponse(TypedDict, closed=True):
    system_summaries: (
        "aws_sdk_resiliencehubv2.types.system_summary_list.SystemSummaryList"
    )
    """<p>The list of system summaries.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSystemsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.system_summary_list

    out["systemSummaries"] = (
        aws_sdk_resiliencehubv2.types.system_summary_list.serialize_json(
            value["system_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSystemsResponse:
    out: ListSystemsResponse = {}  # type: ignore[typeddict-item]
    if "systemSummaries" in data:
        import aws_sdk_resiliencehubv2.types.system_summary_list

        out["system_summaries"] = (
            aws_sdk_resiliencehubv2.types.system_summary_list.deserialize_json(
                data["systemSummaries"]
            )
        )
    else:
        raise DeserializationError("ListSystemsResponse.system_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
