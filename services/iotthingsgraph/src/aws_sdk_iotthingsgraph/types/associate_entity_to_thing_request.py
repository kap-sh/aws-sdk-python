"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#AssociateEntityToThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.thing_name
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.version


class AssociateEntityToThingRequest(TypedDict):
    thing_name: "aws_sdk_iotthingsgraph.types.thing_name.ThingName"
    """<p>The name of the thing to which the entity is to be associated.</p>"""
    entity_id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the device to be associated with the thing.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>"""
    namespace_version: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateEntityToThingRequest) -> dict:
    out: dict = {}
    out["thingName"] = value["thing_name"]
    out["entityId"] = value["entity_id"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateEntityToThingRequest:
    out: AssociateEntityToThingRequest = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    else:
        raise DeserializationError("AssociateEntityToThingRequest.thing_name required")
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("AssociateEntityToThingRequest.entity_id required")
    if "namespaceVersion" in data:
        out["namespace_version"] = data["namespaceVersion"]
    return out
