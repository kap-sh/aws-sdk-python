"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentCategories``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_matched_details


class RealTimeContactAnalysisSegmentCategories(TypedDict):
    matched_details: "aws_sdk_connect.types.real_time_contact_analysis_matched_details.RealTimeContactAnalysisMatchedDetails"
    """<p>Map between the name of the matched rule and RealTimeContactAnalysisCategoryDetails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentCategories) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.real_time_contact_analysis_matched_details

    out["MatchedDetails"] = (
        aws_sdk_connect.types.real_time_contact_analysis_matched_details.serialize_json(
            value["matched_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentCategories:
    out: RealTimeContactAnalysisSegmentCategories = {}  # type: ignore[typeddict-item]
    if "MatchedDetails" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_matched_details

        out["matched_details"] = (
            aws_sdk_connect.types.real_time_contact_analysis_matched_details.deserialize_json(
                data["MatchedDetails"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentCategories.matched_details required"
        )
    return out
