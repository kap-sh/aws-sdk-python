"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisMatchedDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_category_details
    import capo_connect.types.real_time_contact_analysis_category_name

RealTimeContactAnalysisMatchedDetails: TypeAlias = dict[
    "capo_connect.types.real_time_contact_analysis_category_name.RealTimeContactAnalysisCategoryName",
    "capo_connect.types.real_time_contact_analysis_category_details.RealTimeContactAnalysisCategoryDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RealTimeContactAnalysisMatchedDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.real_time_contact_analysis_category_details

        out[key] = (
            capo_connect.types.real_time_contact_analysis_category_details.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisMatchedDetails:
    out: RealTimeContactAnalysisMatchedDetails = {}
    for key, value in data.items():
        import capo_connect.types.real_time_contact_analysis_category_details

        out[key] = (
            capo_connect.types.real_time_contact_analysis_category_details.deserialize_json(
                value
            )
        )
    return out
