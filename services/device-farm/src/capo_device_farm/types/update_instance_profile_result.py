"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateInstanceProfileResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.instance_profile


class UpdateInstanceProfileResult(TypedDict, closed=True):
    instance_profile: NotRequired[
        "capo_device_farm.types.instance_profile.InstanceProfile"
    ]
    """<p>An object that contains information about your instance profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceProfileResult) -> dict:
    out: dict = {}
    if "instance_profile" in value:
        import capo_device_farm.types.instance_profile

        out["instanceProfile"] = (
            capo_device_farm.types.instance_profile.serialize_aws_json_1_1(
                value["instance_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceProfileResult:
    out: UpdateInstanceProfileResult = {}  # type: ignore[typeddict-item]
    if "instanceProfile" in data:
        import capo_device_farm.types.instance_profile

        out["instance_profile"] = (
            capo_device_farm.types.instance_profile.deserialize_aws_json_1_1(
                data["instanceProfile"]
            )
        )
    return out
