"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTConcept``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.string


class SNOMEDCTConcept(TypedDict, closed=True):
    description: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> The description of the SNOMED-CT concept. </p>"""
    code: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> The numeric ID for the SNOMED-CT concept. </p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p> The level of confidence Amazon Comprehend Medical has that the entity should be linked to the identified SNOMED-CT concept. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTConcept) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "code" in value:
        out["Code"] = value["code"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SNOMEDCTConcept:
    out: SNOMEDCTConcept = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Score" in data:
        out["score"] = data["Score"]
    return out
