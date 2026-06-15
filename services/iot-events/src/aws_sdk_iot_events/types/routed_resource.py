"""Generated from Smithy shape ``com.amazonaws.iotevents#RoutedResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.resource_name


class RoutedResource(TypedDict):
    name: NotRequired["aws_sdk_iot_events.types.resource_name.ResourceName"]
    """<p> The name of the routed resource. </p>"""
    arn: NotRequired["aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"]
    r"""<p> The ARN of the routed resource. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutedResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> RoutedResource:
    out: RoutedResource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
