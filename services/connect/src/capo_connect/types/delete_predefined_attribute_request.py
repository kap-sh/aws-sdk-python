"""Generated from Smithy shape ``com.amazonaws.connect#DeletePredefinedAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.predefined_attribute_name


class DeletePredefinedAttributeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p> The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.predefined_attribute_name.PredefinedAttributeName"
    """<p> The name of the predefined attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePredefinedAttributeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePredefinedAttributeRequest:
    out: DeletePredefinedAttributeRequest = {}  # type: ignore[typeddict-item]
    return out
