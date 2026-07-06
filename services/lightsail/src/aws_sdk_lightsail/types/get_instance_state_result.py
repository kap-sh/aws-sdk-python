"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceStateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_state


class GetInstanceStateResult(TypedDict, closed=True):
    state: NotRequired["aws_sdk_lightsail.types.instance_state.InstanceState"]
    """<p>The state of the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceStateResult) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_lightsail.types.instance_state

        out["state"] = aws_sdk_lightsail.types.instance_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceStateResult:
    out: GetInstanceStateResult = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_lightsail.types.instance_state

        out["state"] = aws_sdk_lightsail.types.instance_state.deserialize_aws_json_1_1(
            data["state"]
        )
    return out
