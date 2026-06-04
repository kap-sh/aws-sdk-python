"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service


class UpdateServiceResponse(TypedDict):
    service: NotRequired["aws_sdk_ecs.types.service.Service"]
    """<p>The full description of your service following the update call.</p> <p>The response includes a <code>lifecycleHookDetails</code> field, which is an empty array when the service is created or updated. The values are populated when a lifecycle hook executes and are available as part of the service deployment details (<a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html\">DescribeServiceDeployments</a>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_ecs.types.service

        out["service"] = aws_sdk_ecs.types.service.serialize_aws_json_1_1(
            value["service"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceResponse:
    out: UpdateServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_ecs.types.service

        out["service"] = aws_sdk_ecs.types.service.deserialize_aws_json_1_1(
            data["service"]
        )
    return out
