"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteEndpointAccessRequest``."""

from typing import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError


class DeleteEndpointAccessRequest(TypedDict):
    endpoint_name: "str"
    """<p>The name of the VPC endpoint to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointAccessRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointAccessRequest:
    out: DeleteEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "endpointName" in data:
        out["endpoint_name"] = data["endpointName"]
    else:
        raise DeserializationError("DeleteEndpointAccessRequest.endpoint_name required")
    return out
