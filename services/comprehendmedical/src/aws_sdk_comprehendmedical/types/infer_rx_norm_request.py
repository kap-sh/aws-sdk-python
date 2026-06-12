"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InferRxNormRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string


class InferRxNormRequest(TypedDict):
    text: "aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    """<p>The input text used for analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferRxNormRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferRxNormRequest:
    out: InferRxNormRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("InferRxNormRequest.text required")
    return out
