"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InferICD10CMRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehendmedical.types.ontology_linking_bounded_length_string


class InferICD10CMRequest(TypedDict, closed=True):
    text: "capo_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    """<p>The input text used for analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferICD10CMRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferICD10CMRequest:
    out: InferICD10CMRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("InferICD10CMRequest.text required")
    return out
