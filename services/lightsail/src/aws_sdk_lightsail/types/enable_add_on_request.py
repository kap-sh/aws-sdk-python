"""Generated from Smithy shape ``com.amazonaws.lightsail#EnableAddOnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_request
    import aws_sdk_lightsail.types.resource_name


class EnableAddOnRequest(TypedDict, closed=True):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the source resource for which to enable or modify the add-on.</p>"""
    add_on_request: "aws_sdk_lightsail.types.add_on_request.AddOnRequest"
    """<p>An array of strings representing the add-on to enable or modify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableAddOnRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    import aws_sdk_lightsail.types.add_on_request

    out["addOnRequest"] = aws_sdk_lightsail.types.add_on_request.serialize_aws_json_1_1(
        value["add_on_request"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableAddOnRequest:
    out: EnableAddOnRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("EnableAddOnRequest.resource_name required")
    if "addOnRequest" in data:
        import aws_sdk_lightsail.types.add_on_request

        out["add_on_request"] = (
            aws_sdk_lightsail.types.add_on_request.deserialize_aws_json_1_1(
                data["addOnRequest"]
            )
        )
    else:
        raise DeserializationError("EnableAddOnRequest.add_on_request required")
    return out
