"""Generated from Smithy shape ``com.amazonaws.securityhub#ListStandardsControlAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.standards_control_association_summaries


class ListStandardsControlAssociationsResponse(TypedDict, closed=True):
    standards_control_association_summaries: NotRequired[
        "aws_sdk_securityhub.types.standards_control_association_summaries.StandardsControlAssociationSummaries"
    ]
    """<p> An array that provides the enablement status and other details for each security control that applies to each enabled standard. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> A pagination parameter that's included in the response only if it was included in the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStandardsControlAssociationsResponse) -> dict:
    out: dict = {}
    if "standards_control_association_summaries" in value:
        import aws_sdk_securityhub.types.standards_control_association_summaries

        out["StandardsControlAssociationSummaries"] = (
            aws_sdk_securityhub.types.standards_control_association_summaries.serialize_json(
                value["standards_control_association_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStandardsControlAssociationsResponse:
    out: ListStandardsControlAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "StandardsControlAssociationSummaries" in data:
        import aws_sdk_securityhub.types.standards_control_association_summaries

        out["standards_control_association_summaries"] = (
            aws_sdk_securityhub.types.standards_control_association_summaries.deserialize_json(
                data["StandardsControlAssociationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
