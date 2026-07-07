"""Generated from Smithy shape ``com.amazonaws.batch#UpdateConsumableResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.client_request_token
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class UpdateConsumableResourceRequest(TypedDict, closed=True):
    consumable_resource: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the consumable resource to be updated.</p>"""
    operation: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Indicates how the quantity of the consumable resource will be updated. Must be one of:</p> <ul> <li> <p> <code>SET</code> </p> <p>Sets the quantity of the resource to the value specified by the <code>quantity</code> parameter.</p> </li> <li> <p> <code>ADD</code> </p> <p>Increases the quantity of the resource by the value specified by the <code>quantity</code> parameter.</p> </li> <li> <p> <code>REMOVE</code> </p> <p>Reduces the quantity of the resource by the value specified by the <code>quantity</code> parameter.</p> </li> </ul>"""
    quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The change in the total quantity of the consumable resource. The <code>operation</code> parameter determines whether the value specified here will be the new total quantity, or the amount by which the total quantity will be increased or reduced. Must be a non-negative value.</p>"""
    client_token: NotRequired[
        "aws_sdk_batch.types.client_request_token.ClientRequestToken"
    ]
    """<p>If this parameter is specified and two update requests with identical payloads and <code>clientToken</code>s are received, these requests are considered the same request. Both requests will succeed, but the update will only happen once. A <code>clientToken</code> is valid for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConsumableResourceRequest) -> dict:
    out: dict = {}
    if "consumable_resource" in value:
        out["consumableResource"] = value["consumable_resource"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateConsumableResourceRequest:
    out: UpdateConsumableResourceRequest = {}  # type: ignore[typeddict-item]
    if "consumableResource" in data:
        out["consumable_resource"] = data["consumableResource"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
