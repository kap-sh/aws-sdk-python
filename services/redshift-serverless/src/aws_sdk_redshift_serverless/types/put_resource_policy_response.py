"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.resource_policy


class PutResourcePolicyResponse(TypedDict):
    resource_policy: NotRequired[
        "aws_sdk_redshift_serverless.types.resource_policy.ResourcePolicy"
    ]
    """<p>The policy that was created or updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        import aws_sdk_redshift_serverless.types.resource_policy

        out["resourcePolicy"] = (
            aws_sdk_redshift_serverless.types.resource_policy.serialize_aws_json_1_1(
                value["resource_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourcePolicy" in data:
        import aws_sdk_redshift_serverless.types.resource_policy

        out["resource_policy"] = (
            aws_sdk_redshift_serverless.types.resource_policy.deserialize_aws_json_1_1(
                data["resourcePolicy"]
            )
        )
    return out
