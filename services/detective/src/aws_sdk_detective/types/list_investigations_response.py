"""Generated from Smithy shape ``com.amazonaws.detective#ListInvestigationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.ai_pagination_token
    import aws_sdk_detective.types.investigation_details


class ListInvestigationsResponse(TypedDict):
    investigation_details: NotRequired[
        "aws_sdk_detective.types.investigation_details.InvestigationDetails"
    ]
    """<p>Lists the summary of uncommon behavior or malicious activity which indicates a compromise.</p>"""
    next_token: NotRequired[
        "aws_sdk_detective.types.ai_pagination_token.AiPaginationToken"
    ]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationsResponse) -> dict:
    out: dict = {}
    if "investigation_details" in value:
        import aws_sdk_detective.types.investigation_details

        out["InvestigationDetails"] = (
            aws_sdk_detective.types.investigation_details.serialize_json(
                value["investigation_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvestigationsResponse:
    out: ListInvestigationsResponse = {}  # type: ignore[typeddict-item]
    if "InvestigationDetails" in data:
        import aws_sdk_detective.types.investigation_details

        out["investigation_details"] = (
            aws_sdk_detective.types.investigation_details.deserialize_json(
                data["InvestigationDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
