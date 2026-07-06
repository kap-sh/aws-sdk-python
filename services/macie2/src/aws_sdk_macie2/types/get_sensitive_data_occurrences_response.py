"""Generated from Smithy shape ``com.amazonaws.macie2#GetSensitiveDataOccurrencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.reveal_request_status
    import aws_sdk_macie2.types.sensitive_data_occurrences


class GetSensitiveDataOccurrencesResponse(TypedDict, closed=True):
    error: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>If an error occurred when Amazon Macie attempted to retrieve occurrences of sensitive data reported by the finding, a description of the error that occurred. This value is null if the status (status) of the request is PROCESSING or SUCCESS.</p>"""
    sensitive_data_occurrences: NotRequired[
        "aws_sdk_macie2.types.sensitive_data_occurrences.SensitiveDataOccurrences"
    ]
    """<p>A map that specifies 1-100 types of sensitive data reported by the finding and, for each type, 1-10 occurrences of sensitive data.</p>"""
    status: NotRequired[
        "aws_sdk_macie2.types.reveal_request_status.RevealRequestStatus"
    ]
    """<p>The status of the request to retrieve occurrences of sensitive data reported by the finding. Possible values are:</p> <ul><li><p>ERROR - An error occurred when Amazon Macie attempted to locate, retrieve, or encrypt the sensitive data. The error value indicates the nature of the error that occurred.</p></li> <li><p>PROCESSING - Macie is processing the request.</p></li> <li><p>SUCCESS - Macie successfully located, retrieved, and encrypted the sensitive data.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSensitiveDataOccurrencesResponse) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "sensitive_data_occurrences" in value:
        import aws_sdk_macie2.types.sensitive_data_occurrences

        out["sensitiveDataOccurrences"] = (
            aws_sdk_macie2.types.sensitive_data_occurrences.serialize_json(
                value["sensitive_data_occurrences"]
            )
        )
    if "status" in value:
        import aws_sdk_macie2.types.reveal_request_status

        out["status"] = aws_sdk_macie2.types.reveal_request_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetSensitiveDataOccurrencesResponse:
    out: GetSensitiveDataOccurrencesResponse = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "sensitiveDataOccurrences" in data:
        import aws_sdk_macie2.types.sensitive_data_occurrences

        out["sensitive_data_occurrences"] = (
            aws_sdk_macie2.types.sensitive_data_occurrences.deserialize_json(
                data["sensitiveDataOccurrences"]
            )
        )
    if "status" in data:
        import aws_sdk_macie2.types.reveal_request_status

        out["status"] = aws_sdk_macie2.types.reveal_request_status.deserialize_json(
            data["status"]
        )
    return out
