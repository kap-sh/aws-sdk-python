"""Generated from Smithy shape ``com.amazonaws.securityhub#CustomDataIdentifiersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.custom_data_identifiers_detections_list
    import capo_securityhub.types.long


class CustomDataIdentifiersResult(TypedDict, closed=True):
    detections: NotRequired[
        "capo_securityhub.types.custom_data_identifiers_detections_list.CustomDataIdentifiersDetectionsList"
    ]
    """<p>The list of detected instances of sensitive data.</p>"""
    total_count: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The total number of occurrences of sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifiersResult) -> dict:
    out: dict = {}
    if "detections" in value:
        import capo_securityhub.types.custom_data_identifiers_detections_list

        out["Detections"] = (
            capo_securityhub.types.custom_data_identifiers_detections_list.serialize_json(
                value["detections"]
            )
        )
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> CustomDataIdentifiersResult:
    out: CustomDataIdentifiersResult = {}  # type: ignore[typeddict-item]
    if "Detections" in data:
        import capo_securityhub.types.custom_data_identifiers_detections_list

        out["detections"] = (
            capo_securityhub.types.custom_data_identifiers_detections_list.deserialize_json(
                data["Detections"]
            )
        )
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    return out
