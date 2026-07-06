"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceAccessDetailsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_access_details


class GetInstanceAccessDetailsResult(TypedDict, closed=True):
    access_details: NotRequired[
        "aws_sdk_lightsail.types.instance_access_details.InstanceAccessDetails"
    ]
    """<p>An array of key-value pairs containing information about a get instance access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceAccessDetailsResult) -> dict:
    out: dict = {}
    if "access_details" in value:
        import aws_sdk_lightsail.types.instance_access_details

        out["accessDetails"] = (
            aws_sdk_lightsail.types.instance_access_details.serialize_aws_json_1_1(
                value["access_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceAccessDetailsResult:
    out: GetInstanceAccessDetailsResult = {}  # type: ignore[typeddict-item]
    if "accessDetails" in data:
        import aws_sdk_lightsail.types.instance_access_details

        out["access_details"] = (
            aws_sdk_lightsail.types.instance_access_details.deserialize_aws_json_1_1(
                data["accessDetails"]
            )
        )
    return out
