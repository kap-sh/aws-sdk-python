"""Generated from Smithy shape ``com.amazonaws.securityhub#DataClassificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.classification_result
    import capo_securityhub.types.non_empty_string


class DataClassificationDetails(TypedDict, closed=True):
    detailed_results_location: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The path to the folder or file that contains the sensitive data.</p>"""
    result: NotRequired[
        "capo_securityhub.types.classification_result.ClassificationResult"
    ]
    """<p>The details about the sensitive data that was detected on the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataClassificationDetails) -> dict:
    out: dict = {}
    if "detailed_results_location" in value:
        out["DetailedResultsLocation"] = value["detailed_results_location"]
    if "result" in value:
        import capo_securityhub.types.classification_result

        out["Result"] = capo_securityhub.types.classification_result.serialize_json(
            value["result"]
        )
    return out


def deserialize_json(data: dict) -> DataClassificationDetails:
    out: DataClassificationDetails = {}  # type: ignore[typeddict-item]
    if "DetailedResultsLocation" in data:
        out["detailed_results_location"] = data["DetailedResultsLocation"]
    if "Result" in data:
        import capo_securityhub.types.classification_result

        out["result"] = capo_securityhub.types.classification_result.deserialize_json(
            data["Result"]
        )
    return out
