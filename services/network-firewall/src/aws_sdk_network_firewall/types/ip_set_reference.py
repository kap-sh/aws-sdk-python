"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSetReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn


class IPSetReference(TypedDict):
    reference_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource that you are referencing in your rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IPSetReference) -> dict:
    out: dict = {}
    if "reference_arn" in value:
        out["ReferenceArn"] = value["reference_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSetReference:
    out: IPSetReference = {}  # type: ignore[typeddict-item]
    if "ReferenceArn" in data:
        out["reference_arn"] = data["ReferenceArn"]
    return out
