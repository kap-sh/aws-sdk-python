"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateDetectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.unprocessed_data_sources_result


class CreateDetectorResponse(TypedDict):
    detector_id: NotRequired["aws_sdk_guardduty.types.detector_id.DetectorId"]
    """<p>The unique ID of the created detector.</p>"""
    unprocessed_data_sources: NotRequired[
        "aws_sdk_guardduty.types.unprocessed_data_sources_result.UnprocessedDataSourcesResult"
    ]
    """<p>Specifies the data sources that couldn't be enabled when GuardDuty was enabled for the first time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDetectorResponse) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "unprocessed_data_sources" in value:
        import aws_sdk_guardduty.types.unprocessed_data_sources_result

        out["unprocessedDataSources"] = (
            aws_sdk_guardduty.types.unprocessed_data_sources_result.serialize_json(
                value["unprocessed_data_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDetectorResponse:
    out: CreateDetectorResponse = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "unprocessedDataSources" in data:
        import aws_sdk_guardduty.types.unprocessed_data_sources_result

        out["unprocessed_data_sources"] = (
            aws_sdk_guardduty.types.unprocessed_data_sources_result.deserialize_json(
                data["unprocessedDataSources"]
            )
        )
    return out
