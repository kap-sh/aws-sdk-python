"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetExternalModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_models_max_results
    import aws_sdk_frauddetector.types.string


class GetExternalModelsRequest(TypedDict):
    model_endpoint: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The Amazon SageMaker model endpoint.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token for the request.</p>"""
    max_results: NotRequired[
        "aws_sdk_frauddetector.types.external_models_max_results.ExternalModelsMaxResults"
    ]
    """<p>The maximum number of objects to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExternalModelsRequest) -> dict:
    out: dict = {}
    if "model_endpoint" in value:
        out["modelEndpoint"] = value["model_endpoint"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExternalModelsRequest:
    out: GetExternalModelsRequest = {}  # type: ignore[typeddict-item]
    if "modelEndpoint" in data:
        out["model_endpoint"] = data["modelEndpoint"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
