"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMConcept``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.string


class ICD10CMConcept(TypedDict):
    description: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>The long description of the ICD-10-CM code in the ontology.</p>"""
    code: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>The ICD-10-CM code that identifies the concept found in the knowledge base from the Centers for Disease Control.</p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to an ICD-10-CM concept.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMConcept) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "code" in value:
        out["Code"] = value["code"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ICD10CMConcept:
    out: ICD10CMConcept = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Score" in data:
        out["score"] = data["Score"]
    return out
