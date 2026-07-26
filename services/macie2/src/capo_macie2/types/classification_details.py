"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.classification_result
    import capo_macie2.types.origin_type


class ClassificationDetails(TypedDict, closed=True):
    detailed_results_location: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The path to the folder or file in Amazon S3 that contains the corresponding sensitive data discovery result for the finding. If a finding applies to a large archive or compressed file, this value is the path to a folder. Otherwise, this value is the path to a file.</p>"""
    job_arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the classification job that produced the finding. This value is null if the origin of the finding (originType) is AUTOMATED_SENSITIVE_DATA_DISCOVERY.</p>"""
    job_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the classification job that produced the finding. This value is null if the origin of the finding (originType) is AUTOMATED_SENSITIVE_DATA_DISCOVERY.</p>"""
    origin_type: NotRequired["capo_macie2.types.origin_type.OriginType"]
    """<p>Specifies how Amazon Macie found the sensitive data that produced the finding. Possible values are: SENSITIVE_DATA_DISCOVERY_JOB, for a classification job; and, AUTOMATED_SENSITIVE_DATA_DISCOVERY, for automated sensitive data discovery.</p>"""
    result: NotRequired["capo_macie2.types.classification_result.ClassificationResult"]
    """<p>The status and other details of the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationDetails) -> dict:
    out: dict = {}
    if "detailed_results_location" in value:
        out["detailedResultsLocation"] = value["detailed_results_location"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "origin_type" in value:
        import capo_macie2.types.origin_type

        out["originType"] = capo_macie2.types.origin_type.serialize_json(
            value["origin_type"]
        )
    if "result" in value:
        import capo_macie2.types.classification_result

        out["result"] = capo_macie2.types.classification_result.serialize_json(
            value["result"]
        )
    return out


def deserialize_json(data: dict) -> ClassificationDetails:
    out: ClassificationDetails = {}  # type: ignore[typeddict-item]
    if "detailedResultsLocation" in data:
        out["detailed_results_location"] = data["detailedResultsLocation"]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "originType" in data:
        import capo_macie2.types.origin_type

        out["origin_type"] = capo_macie2.types.origin_type.deserialize_json(
            data["originType"]
        )
    if "result" in data:
        import capo_macie2.types.classification_result

        out["result"] = capo_macie2.types.classification_result.deserialize_json(
            data["result"]
        )
    return out
