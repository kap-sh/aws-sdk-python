"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateSampleFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.finding_types


class CreateSampleFindingsRequest(TypedDict, closed=True):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The ID of the detector for which you need to create sample findings.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    finding_types: NotRequired["aws_sdk_guardduty.types.finding_types.FindingTypes"]
    """<p>The types of sample findings to generate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSampleFindingsRequest) -> dict:
    out: dict = {}
    if "finding_types" in value:
        import aws_sdk_guardduty.types.finding_types

        out["findingTypes"] = aws_sdk_guardduty.types.finding_types.serialize_json(
            value["finding_types"]
        )
    return out


def deserialize_json(data: dict) -> CreateSampleFindingsRequest:
    out: CreateSampleFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingTypes" in data:
        import aws_sdk_guardduty.types.finding_types

        out["finding_types"] = aws_sdk_guardduty.types.finding_types.deserialize_json(
            data["findingTypes"]
        )
    return out
