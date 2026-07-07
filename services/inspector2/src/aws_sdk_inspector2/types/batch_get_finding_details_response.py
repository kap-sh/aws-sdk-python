"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetFindingDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.finding_details
    import aws_sdk_inspector2.types.finding_details_error_list


class BatchGetFindingDetailsResponse(TypedDict, closed=True):
    finding_details: NotRequired[
        "aws_sdk_inspector2.types.finding_details.FindingDetails"
    ]
    """<p>A finding's vulnerability details.</p>"""
    errors: NotRequired[
        "aws_sdk_inspector2.types.finding_details_error_list.FindingDetailsErrorList"
    ]
    """<p>Error information for findings that details could not be returned for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingDetailsResponse) -> dict:
    out: dict = {}
    if "finding_details" in value:
        import aws_sdk_inspector2.types.finding_details

        out["findingDetails"] = aws_sdk_inspector2.types.finding_details.serialize_json(
            value["finding_details"]
        )
    if "errors" in value:
        import aws_sdk_inspector2.types.finding_details_error_list

        out["errors"] = (
            aws_sdk_inspector2.types.finding_details_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetFindingDetailsResponse:
    out: BatchGetFindingDetailsResponse = {}  # type: ignore[typeddict-item]
    if "findingDetails" in data:
        import aws_sdk_inspector2.types.finding_details

        out["finding_details"] = (
            aws_sdk_inspector2.types.finding_details.deserialize_json(
                data["findingDetails"]
            )
        )
    if "errors" in data:
        import aws_sdk_inspector2.types.finding_details_error_list

        out["errors"] = (
            aws_sdk_inspector2.types.finding_details_error_list.deserialize_json(
                data["errors"]
            )
        )
    return out
