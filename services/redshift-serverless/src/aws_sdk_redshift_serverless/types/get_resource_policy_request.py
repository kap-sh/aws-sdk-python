"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetResourcePolicyRequest``."""

from typing import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError


class GetResourcePolicyRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyRequest.resource_arn required")
    return out
