"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.string


class SNOMEDCTDetails(TypedDict):
    edition: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> The edition of SNOMED-CT used. The edition used for the InferSNOMEDCT editions is the US edition. </p>"""
    language: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> The language used in the SNOMED-CT ontology. All Amazon Comprehend Medical operations are US English (en). </p>"""
    version_date: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> The version date of the SNOMED-CT ontology used. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTDetails) -> dict:
    out: dict = {}
    if "edition" in value:
        out["Edition"] = value["edition"]
    if "language" in value:
        out["Language"] = value["language"]
    if "version_date" in value:
        out["VersionDate"] = value["version_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SNOMEDCTDetails:
    out: SNOMEDCTDetails = {}  # type: ignore[typeddict-item]
    if "Edition" in data:
        out["edition"] = data["Edition"]
    if "Language" in data:
        out["language"] = data["Language"]
    if "VersionDate" in data:
        out["version_date"] = data["VersionDate"]
    return out
