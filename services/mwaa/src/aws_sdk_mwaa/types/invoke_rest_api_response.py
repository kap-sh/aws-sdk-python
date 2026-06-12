"""Generated from Smithy shape ``com.amazonaws.mwaa#InvokeRestApiResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mwaa.types.rest_api_response

class InvokeRestApiResponse(TypedDict):
    rest_api_status_code: NotRequired["int"]
    """<p>The HTTP status code returned by the Apache Airflow REST API call.</p>"""
    rest_api_response: NotRequired["aws_sdk_mwaa.types.rest_api_response.RestApiResponse"]
    """<p>The response data from the Apache Airflow REST API call, provided as a JSON object.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: InvokeRestApiResponse) -> dict:
    out: dict = {}
    if "rest_api_status_code" in value:
        out["RestApiStatusCode"] = value["rest_api_status_code"]
    if "rest_api_response" in value:
        out["RestApiResponse"] = value["rest_api_response"]
    return out


def deserialize_json(data: dict) -> InvokeRestApiResponse:
    out: InvokeRestApiResponse = {}  # type: ignore[typeddict-item]
    if "RestApiStatusCode" in data:
        out["rest_api_status_code"] = data["RestApiStatusCode"]
    if "RestApiResponse" in data:
        out["rest_api_response"] = data["RestApiResponse"]
    return out