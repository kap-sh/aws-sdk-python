"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.resource_policy


class GetResourcePolicyResponse(TypedDict):
    resource_policy: NotRequired[
        "aws_sdk_redshift_serverless.types.resource_policy.ResourcePolicy"
    ]
    """<p>The returned resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        import aws_sdk_redshift_serverless.types.resource_policy

        out["resourcePolicy"] = (
            aws_sdk_redshift_serverless.types.resource_policy.serialize_aws_json_1_1(
                value["resource_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourcePolicy" in data:
        import aws_sdk_redshift_serverless.types.resource_policy

        out["resource_policy"] = (
            aws_sdk_redshift_serverless.types.resource_policy.deserialize_aws_json_1_1(
                data["resourcePolicy"]
            )
        )
    return out
