"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteResourcePolicyRequest``."""

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the policy to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    return out
