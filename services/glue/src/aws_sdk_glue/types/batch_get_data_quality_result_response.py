"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityResultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_result_ids
    import aws_sdk_glue.types.data_quality_results_list


class BatchGetDataQualityResultResponse(TypedDict, closed=True):
    results: "aws_sdk_glue.types.data_quality_results_list.DataQualityResultsList"
    """<p>A list of <code>DataQualityResult</code> objects representing the data quality results.</p>"""
    results_not_found: NotRequired[
        "aws_sdk_glue.types.data_quality_result_ids.DataQualityResultIds"
    ]
    """<p>A list of result IDs for which results were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDataQualityResultResponse) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.data_quality_results_list

    out["Results"] = (
        aws_sdk_glue.types.data_quality_results_list.serialize_aws_json_1_1(
            value["results"]
        )
    )
    if "results_not_found" in value:
        import aws_sdk_glue.types.data_quality_result_ids

        out["ResultsNotFound"] = (
            aws_sdk_glue.types.data_quality_result_ids.serialize_aws_json_1_1(
                value["results_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDataQualityResultResponse:
    out: BatchGetDataQualityResultResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_glue.types.data_quality_results_list

        out["results"] = (
            aws_sdk_glue.types.data_quality_results_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        raise DeserializationError("BatchGetDataQualityResultResponse.results required")
    if "ResultsNotFound" in data:
        import aws_sdk_glue.types.data_quality_result_ids

        out["results_not_found"] = (
            aws_sdk_glue.types.data_quality_result_ids.deserialize_aws_json_1_1(
                data["ResultsNotFound"]
            )
        )
    return out
