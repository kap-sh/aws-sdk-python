"""Generated from Smithy shape ``com.amazonaws.frauddetector#DescribeModelVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float_version_string
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum
    import capo_frauddetector.types.models_max_page_size
    import capo_frauddetector.types.string


class DescribeModelVersionsRequest(TypedDict, closed=True):
    model_id: NotRequired["capo_frauddetector.types.model_identifier.modelIdentifier"]
    """<p>The model ID.</p>"""
    model_version_number: NotRequired[
        "capo_frauddetector.types.float_version_string.floatVersionString"
    ]
    """<p>The model version number.</p>"""
    model_type: NotRequired["capo_frauddetector.types.model_type_enum.ModelTypeEnum"]
    """<p>The model type.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token from the previous results.</p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.models_max_page_size.modelsMaxPageSize"
    ]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelVersionsRequest) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "model_version_number" in value:
        out["modelVersionNumber"] = value["model_version_number"]
    if "model_type" in value:
        import capo_frauddetector.types.model_type_enum

        out["modelType"] = (
            capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
                value["model_type"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelVersionsRequest:
    out: DescribeModelVersionsRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    if "modelType" in data:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
