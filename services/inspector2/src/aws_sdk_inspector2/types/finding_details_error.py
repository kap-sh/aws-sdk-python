"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingDetailsError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.finding_arn
    import aws_sdk_inspector2.types.finding_details_error_code
    import aws_sdk_inspector2.types.non_empty_string


class FindingDetailsError(TypedDict):
    finding_arn: "aws_sdk_inspector2.types.finding_arn.FindingArn"
    """<p>The finding ARN that returned an error.</p>"""
    error_code: (
        "aws_sdk_inspector2.types.finding_details_error_code.FindingDetailsErrorCode"
    )
    """<p>The error code.</p>"""
    error_message: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetailsError) -> dict:
    out: dict = {}
    out["findingArn"] = value["finding_arn"]
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FindingDetailsError:
    out: FindingDetailsError = {}  # type: ignore[typeddict-item]
    if "findingArn" in data:
        out["finding_arn"] = data["findingArn"]
    else:
        raise DeserializationError("FindingDetailsError.finding_arn required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("FindingDetailsError.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("FindingDetailsError.error_message required")
    return out
