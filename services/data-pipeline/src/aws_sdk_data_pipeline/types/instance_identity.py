"""Generated from Smithy shape ``com.amazonaws.datapipeline#InstanceIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.string


class InstanceIdentity(TypedDict, closed=True):
    document: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>A description of an EC2 instance that is generated when the instance is launched and exposed to the instance via the instance metadata service in the form of a JSON representation of an object.</p>"""
    signature: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>A signature which can be used to verify the accuracy and authenticity of the information provided in the instance identity document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceIdentity) -> dict:
    out: dict = {}
    if "document" in value:
        out["document"] = value["document"]
    if "signature" in value:
        out["signature"] = value["signature"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceIdentity:
    out: InstanceIdentity = {}  # type: ignore[typeddict-item]
    if "document" in data:
        out["document"] = data["document"]
    if "signature" in data:
        out["signature"] = data["signature"]
    return out
