"""Generated from Smithy shape ``com.amazonaws.ssmsap#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.arn
    import capo_ssm_sap.types.operation_event_resource_type


class Resource(TypedDict, closed=True):
    resource_arn: NotRequired["capo_ssm_sap.types.arn.Arn"]
    r"""<p>The Amazon Resource Name (ARN) of the source resource.</p> <p>Example of <code>ResourceArn</code>: \"<code>arn:aws:ec2:us-east-1:111111111111:instance/i-abcdefgh987654321</code>\"</p>"""
    resource_type: NotRequired[
        "capo_ssm_sap.types.operation_event_resource_type.OperationEventResourceType"
    ]
    r"""<p>The resource type.</p> <p>Example of <code>ResourceType</code>: \"<code>AWS::SystemsManagerSAP::Component</code>\" or \"<code>AWS::EC2::Instance</code>\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
