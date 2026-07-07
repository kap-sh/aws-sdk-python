"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetInstanceProfileResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.instance_profile


class GetInstanceProfileResult(TypedDict, closed=True):
    instance_profile: NotRequired[
        "aws_sdk_device_farm.types.instance_profile.InstanceProfile"
    ]
    """<p>An object that contains information about an instance profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceProfileResult) -> dict:
    out: dict = {}
    if "instance_profile" in value:
        import aws_sdk_device_farm.types.instance_profile

        out["instanceProfile"] = (
            aws_sdk_device_farm.types.instance_profile.serialize_aws_json_1_1(
                value["instance_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceProfileResult:
    out: GetInstanceProfileResult = {}  # type: ignore[typeddict-item]
    if "instanceProfile" in data:
        import aws_sdk_device_farm.types.instance_profile

        out["instance_profile"] = (
            aws_sdk_device_farm.types.instance_profile.deserialize_aws_json_1_1(
                data["instanceProfile"]
            )
        )
    return out
