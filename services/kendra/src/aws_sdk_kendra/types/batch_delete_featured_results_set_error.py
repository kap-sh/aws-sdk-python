"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteFeaturedResultsSetError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.error_code
    import aws_sdk_kendra.types.error_message
    import aws_sdk_kendra.types.featured_results_set_id


class BatchDeleteFeaturedResultsSetError(TypedDict, closed=True):
    id: "aws_sdk_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    """<p>The identifier of the set of featured results that couldn't be removed from the index.</p>"""
    error_code: "aws_sdk_kendra.types.error_code.ErrorCode"
    """<p>The error code for why the set of featured results couldn't be removed from the index.</p>"""
    error_message: "aws_sdk_kendra.types.error_message.ErrorMessage"
    """<p>An explanation for why the set of featured results couldn't be removed from the index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFeaturedResultsSetError) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_kendra.types.error_code

    out["ErrorCode"] = aws_sdk_kendra.types.error_code.serialize_aws_json_1_1(
        value["error_code"]
    )
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteFeaturedResultsSetError:
    out: BatchDeleteFeaturedResultsSetError = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("BatchDeleteFeaturedResultsSetError.id required")
    if "ErrorCode" in data:
        import aws_sdk_kendra.types.error_code

        out["error_code"] = aws_sdk_kendra.types.error_code.deserialize_aws_json_1_1(
            data["ErrorCode"]
        )
    else:
        raise DeserializationError(
            "BatchDeleteFeaturedResultsSetError.error_code required"
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "BatchDeleteFeaturedResultsSetError.error_message required"
        )
    return out
