"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetDetectorsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.detector_list
    import capo_frauddetector.types.string


class GetDetectorsResult(TypedDict, closed=True):
    detectors: NotRequired["capo_frauddetector.types.detector_list.DetectorList"]
    """<p>The detectors.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDetectorsResult) -> dict:
    out: dict = {}
    if "detectors" in value:
        import capo_frauddetector.types.detector_list

        out["detectors"] = (
            capo_frauddetector.types.detector_list.serialize_aws_json_1_1(
                value["detectors"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDetectorsResult:
    out: GetDetectorsResult = {}  # type: ignore[typeddict-item]
    if "detectors" in data:
        import capo_frauddetector.types.detector_list

        out["detectors"] = (
            capo_frauddetector.types.detector_list.deserialize_aws_json_1_1(
                data["detectors"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
