"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdatePublishingDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.destination_properties
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.string


class UpdatePublishingDestinationRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector associated with the publishing destinations to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    destination_id: "aws_sdk_guardduty.types.string.String"
    """<p>The ID of the publishing destination to update.</p>"""
    destination_properties: NotRequired[
        "aws_sdk_guardduty.types.destination_properties.DestinationProperties"
    ]
    """<p>A <code>DestinationProperties</code> object that includes the <code>DestinationArn</code> and <code>KmsKeyArn</code> of the publishing destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePublishingDestinationRequest) -> dict:
    out: dict = {}
    if "destination_properties" in value:
        import aws_sdk_guardduty.types.destination_properties

        out["destinationProperties"] = (
            aws_sdk_guardduty.types.destination_properties.serialize_json(
                value["destination_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePublishingDestinationRequest:
    out: UpdatePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
    if "destinationProperties" in data:
        import aws_sdk_guardduty.types.destination_properties

        out["destination_properties"] = (
            aws_sdk_guardduty.types.destination_properties.deserialize_json(
                data["destinationProperties"]
            )
        )
    return out
