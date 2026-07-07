"""Generated from Smithy shape ``com.amazonaws.b2bi#GenerateMappingResponse``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError


class GenerateMappingResponse(TypedDict, closed=True):
    mapping_template: "str"
    """<p>Returns a mapping template based on your inputs.</p>"""
    mapping_accuracy: NotRequired["float"]
    """<p>Returns a percentage that estimates the accuracy of the generated mapping.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GenerateMappingResponse) -> dict:
    out: dict = {}
    out["mappingTemplate"] = value["mapping_template"]
    if "mapping_accuracy" in value:
        out["mappingAccuracy"] = value["mapping_accuracy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GenerateMappingResponse:
    out: GenerateMappingResponse = {}  # type: ignore[typeddict-item]
    if "mappingTemplate" in data:
        out["mapping_template"] = data["mappingTemplate"]
    else:
        raise DeserializationError("GenerateMappingResponse.mapping_template required")
    if "mappingAccuracy" in data:
        out["mapping_accuracy"] = data["mappingAccuracy"]
    return out
