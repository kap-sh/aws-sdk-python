"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlMappingDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.common_control_arn


class CommonControlMappingDetails(TypedDict):
    common_control_arn: (
        "aws_sdk_controlcatalog.types.common_control_arn.CommonControlArn"
    )
    """<p>The Amazon Resource Name (ARN) that identifies the common control in the mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlMappingDetails) -> dict:
    out: dict = {}
    out["CommonControlArn"] = value["common_control_arn"]
    return out


def deserialize_json(data: dict) -> CommonControlMappingDetails:
    out: CommonControlMappingDetails = {}  # type: ignore[typeddict-item]
    if "CommonControlArn" in data:
        out["common_control_arn"] = data["CommonControlArn"]
    else:
        raise DeserializationError(
            "CommonControlMappingDetails.common_control_arn required"
        )
    return out
