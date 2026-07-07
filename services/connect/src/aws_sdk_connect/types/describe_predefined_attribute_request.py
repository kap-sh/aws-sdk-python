"""Generated from Smithy shape ``com.amazonaws.connect#DescribePredefinedAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.predefined_attribute_name


class DescribePredefinedAttributeRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.predefined_attribute_name.PredefinedAttributeName"
    """<p>The name of the predefined attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePredefinedAttributeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePredefinedAttributeRequest:
    out: DescribePredefinedAttributeRequest = {}  # type: ignore[typeddict-item]
    return out
