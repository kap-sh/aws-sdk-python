"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteFeaturedResultsSetErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.batch_delete_featured_results_set_error

BatchDeleteFeaturedResultsSetErrors: TypeAlias = list[
    "capo_kendra.types.batch_delete_featured_results_set_error.BatchDeleteFeaturedResultsSetError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFeaturedResultsSetErrors) -> list:
    import capo_kendra.types.batch_delete_featured_results_set_error

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.batch_delete_featured_results_set_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteFeaturedResultsSetErrors:
    import capo_kendra.types.batch_delete_featured_results_set_error

    out: BatchDeleteFeaturedResultsSetErrors = []
    for item in data:
        out.append(
            capo_kendra.types.batch_delete_featured_results_set_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
