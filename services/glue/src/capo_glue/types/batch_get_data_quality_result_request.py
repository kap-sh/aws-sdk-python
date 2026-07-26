"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityResultRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result_ids


class BatchGetDataQualityResultRequest(TypedDict, closed=True):
    result_ids: "capo_glue.types.data_quality_result_ids.DataQualityResultIds"
    """<p>A list of unique result IDs for the data quality results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDataQualityResultRequest) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_result_ids

    out["ResultIds"] = capo_glue.types.data_quality_result_ids.serialize_aws_json_1_1(
        value["result_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDataQualityResultRequest:
    out: BatchGetDataQualityResultRequest = {}  # type: ignore[typeddict-item]
    if "ResultIds" in data:
        import capo_glue.types.data_quality_result_ids

        out["result_ids"] = (
            capo_glue.types.data_quality_result_ids.deserialize_aws_json_1_1(
                data["ResultIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDataQualityResultRequest.result_ids required"
        )
    return out
