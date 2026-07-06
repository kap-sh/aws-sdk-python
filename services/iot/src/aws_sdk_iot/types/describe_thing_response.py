"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.attributes
    import aws_sdk_iot.types.billing_group_name
    import aws_sdk_iot.types.client_id
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.thing_id
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_type_name
    import aws_sdk_iot.types.version


class DescribeThingResponse(TypedDict, closed=True):
    default_client_id: NotRequired["aws_sdk_iot.types.client_id.ClientId"]
    """<p>The default MQTT client ID. For a typical device, the thing name is also used as the default MQTT client ID. Although we don’t require a mapping between a thing's registry name and its use of MQTT client IDs, certificates, or shadow state, we recommend that you choose a thing name and use it as the MQTT client ID for the registry and the Device Shadow service.</p> <p>This lets you better organize your IoT fleet without removing the flexibility of the underlying device certificate model or shadows.</p>"""
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The name of the thing.</p>"""
    thing_id: NotRequired["aws_sdk_iot.types.thing_id.ThingId"]
    """<p>The ID of the thing to describe.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing to describe.</p>"""
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The thing type name.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.attributes.Attributes"]
    """<p>The thing attributes.</p>"""
    version: "aws_sdk_iot.types.version.Version"
    """<p>The current version of the thing record in the registry.</p> <note> <p>To avoid unintentional changes to the information in the registry, you can pass the version information in the <code>expectedVersion</code> parameter of the <code>UpdateThing</code> and <code>DeleteThing</code> calls.</p> </note>"""
    billing_group_name: NotRequired[
        "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group the thing belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingResponse) -> dict:
    out: dict = {}
    if "default_client_id" in value:
        out["defaultClientId"] = value["default_client_id"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_id" in value:
        out["thingId"] = value["thing_id"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "attributes" in value:
        import aws_sdk_iot.types.attributes

        out["attributes"] = aws_sdk_iot.types.attributes.serialize_json(
            value["attributes"]
        )
    out["version"] = value.get("version", 0)
    if "billing_group_name" in value:
        out["billingGroupName"] = value["billing_group_name"]
    return out


def deserialize_json(data: dict) -> DescribeThingResponse:
    out: DescribeThingResponse = {}  # type: ignore[typeddict-item]
    if "defaultClientId" in data:
        out["default_client_id"] = data["defaultClientId"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingId" in data:
        out["thing_id"] = data["thingId"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    if "thingTypeName" in data:
        out["thing_type_name"] = data["thingTypeName"]
    if "attributes" in data:
        import aws_sdk_iot.types.attributes

        out["attributes"] = aws_sdk_iot.types.attributes.deserialize_json(
            data["attributes"]
        )
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if "billingGroupName" in data:
        out["billing_group_name"] = data["billingGroupName"]
    return out
