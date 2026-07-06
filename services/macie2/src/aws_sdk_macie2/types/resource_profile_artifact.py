"""Generated from Smithy shape ``com.amazonaws.macie2#ResourceProfileArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__string


class ResourceProfileArtifact(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the object.</p>"""
    classification_result_status: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The status of the analysis. Possible values are:</p> <ul><li><p>COMPLETE - Amazon Macie successfully completed its analysis of the object.</p></li> <li><p>PARTIAL - Macie analyzed only a subset of data in the object. For example, the object is an archive file that contains files in an unsupported format.</p></li> <li><p>SKIPPED - Macie wasn't able to analyze the object. For example, the object is a malformed file.</p></li></ul>"""
    sensitive: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether Amazon Macie found sensitive data in the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceProfileArtifact) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "classification_result_status" in value:
        out["classificationResultStatus"] = value["classification_result_status"]
    if "sensitive" in value:
        out["sensitive"] = value["sensitive"]
    return out


def deserialize_json(data: dict) -> ResourceProfileArtifact:
    out: ResourceProfileArtifact = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "classificationResultStatus" in data:
        out["classification_result_status"] = data["classificationResultStatus"]
    if "sensitive" in data:
        out["sensitive"] = data["sensitive"]
    return out
