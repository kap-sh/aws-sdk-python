"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDedicatedIpPoolScalingAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.pool_name
    import aws_sdk_sesv2.types.scaling_mode


class PutDedicatedIpPoolScalingAttributesRequest(TypedDict):
    pool_name: "aws_sdk_sesv2.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool.</p>"""
    scaling_mode: "aws_sdk_sesv2.types.scaling_mode.ScalingMode"
    """<p>The scaling mode to apply to the dedicated IP pool.</p> <note> <p>Changing the scaling mode from <code>MANAGED</code> to <code>STANDARD</code> is not supported.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpPoolScalingAttributesRequest) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.scaling_mode

    out["ScalingMode"] = aws_sdk_sesv2.types.scaling_mode.serialize_json(
        value["scaling_mode"]
    )
    return out


def deserialize_json(data: dict) -> PutDedicatedIpPoolScalingAttributesRequest:
    out: PutDedicatedIpPoolScalingAttributesRequest = {}  # type: ignore[typeddict-item]
    if "ScalingMode" in data:
        import aws_sdk_sesv2.types.scaling_mode

        out["scaling_mode"] = aws_sdk_sesv2.types.scaling_mode.deserialize_json(
            data["ScalingMode"]
        )
    else:
        raise DeserializationError(
            "PutDedicatedIpPoolScalingAttributesRequest.scaling_mode required"
        )
    return out
