"""Generated from Smithy shape ``com.amazonaws.lightsail#DisableAddOnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_type
    import aws_sdk_lightsail.types.resource_name


class DisableAddOnRequest(TypedDict, closed=True):
    add_on_type: "aws_sdk_lightsail.types.add_on_type.AddOnType"
    """<p>The add-on type to disable.</p>"""
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the source resource for which to disable the add-on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableAddOnRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.add_on_type

    out["addOnType"] = aws_sdk_lightsail.types.add_on_type.serialize_aws_json_1_1(
        value["add_on_type"]
    )
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableAddOnRequest:
    out: DisableAddOnRequest = {}  # type: ignore[typeddict-item]
    if "addOnType" in data:
        import aws_sdk_lightsail.types.add_on_type

        out["add_on_type"] = (
            aws_sdk_lightsail.types.add_on_type.deserialize_aws_json_1_1(
                data["addOnType"]
            )
        )
    else:
        raise DeserializationError("DisableAddOnRequest.add_on_type required")
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("DisableAddOnRequest.resource_name required")
    return out
