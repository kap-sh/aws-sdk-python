"""Generated from Smithy shape ``com.amazonaws.kendra#RelevanceFeedback``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.relevance_type
    import aws_sdk_kendra.types.result_id


class RelevanceFeedback(TypedDict, closed=True):
    result_id: "aws_sdk_kendra.types.result_id.ResultId"
    """<p>The identifier of the search result that the user provided relevance feedback for.</p>"""
    relevance_value: "aws_sdk_kendra.types.relevance_type.RelevanceType"
    """<p>Whether the document was relevant or not relevant to the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelevanceFeedback) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    import aws_sdk_kendra.types.relevance_type

    out["RelevanceValue"] = aws_sdk_kendra.types.relevance_type.serialize_aws_json_1_1(
        value["relevance_value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelevanceFeedback:
    out: RelevanceFeedback = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    else:
        raise DeserializationError("RelevanceFeedback.result_id required")
    if "RelevanceValue" in data:
        import aws_sdk_kendra.types.relevance_type

        out["relevance_value"] = (
            aws_sdk_kendra.types.relevance_type.deserialize_aws_json_1_1(
                data["RelevanceValue"]
            )
        )
    else:
        raise DeserializationError("RelevanceFeedback.relevance_value required")
    return out
