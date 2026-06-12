"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#VpcConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.vpc_id


class VpcConfiguration(TypedDict):
    vpc_id: "aws_sdk_accessanalyzer.types.vpc_id.VpcId"
    """<p> If this field is specified, this access point will only allow connections from the specified VPC ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("VpcConfiguration.vpc_id required")
    return out
