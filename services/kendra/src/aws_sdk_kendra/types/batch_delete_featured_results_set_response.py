"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteFeaturedResultsSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.batch_delete_featured_results_set_errors


class BatchDeleteFeaturedResultsSetResponse(TypedDict):
    errors: "aws_sdk_kendra.types.batch_delete_featured_results_set_errors.BatchDeleteFeaturedResultsSetErrors"
    """<p>The list of errors for the featured results set IDs, explaining why they couldn't be removed from the index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFeaturedResultsSetResponse) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.batch_delete_featured_results_set_errors

    out["Errors"] = (
        aws_sdk_kendra.types.batch_delete_featured_results_set_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteFeaturedResultsSetResponse:
    out: BatchDeleteFeaturedResultsSetResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_kendra.types.batch_delete_featured_results_set_errors

        out["errors"] = (
            aws_sdk_kendra.types.batch_delete_featured_results_set_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteFeaturedResultsSetResponse.errors required"
        )
    return out
