"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositeModelProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property


class CompositeModelProperty(TypedDict, closed=True):
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the property.</p>"""
    type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The type of the composite model that defines this property.</p>"""
    asset_property: "aws_sdk_iotsitewise.types.property.Property"
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p> The ID of the composite model that contains the property. </p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>The external ID of the composite model that contains the property. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeModelProperty) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    import aws_sdk_iotsitewise.types.property

    out["assetProperty"] = aws_sdk_iotsitewise.types.property.serialize_json(
        value["asset_property"]
    )
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> CompositeModelProperty:
    out: CompositeModelProperty = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CompositeModelProperty.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CompositeModelProperty.type required")
    if "assetProperty" in data:
        import aws_sdk_iotsitewise.types.property

        out["asset_property"] = aws_sdk_iotsitewise.types.property.deserialize_json(
            data["assetProperty"]
        )
    else:
        raise DeserializationError("CompositeModelProperty.asset_property required")
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    return out
