"""Generated from Smithy shape ``com.amazonaws.frauddetector#PutDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.tag_list


class PutDetectorRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID. </p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The description of the detector.</p>"""
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDetectorRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["eventTypeName"] = value["event_type_name"]
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDetectorRequest:
    out: PutDetectorRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("PutDetectorRequest.detector_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError("PutDetectorRequest.event_type_name required")
    if "tags" in data:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
