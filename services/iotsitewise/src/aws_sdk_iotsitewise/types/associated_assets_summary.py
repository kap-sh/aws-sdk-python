"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssociatedAssetsSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.asset_hierarchies
    import aws_sdk_iotsitewise.types.asset_status
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.timestamp


class AssociatedAssetsSummary(TypedDict):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>The external ID of the asset. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the asset, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}</code> </p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the asset.</p>"""
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model used to create the asset.</p>"""
    creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was created, in Unix epoch time.</p>"""
    last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was last updated, in Unix epoch time.</p>"""
    status: "aws_sdk_iotsitewise.types.asset_status.AssetStatus"
    """<p>The current status of the asset.</p>"""
    hierarchies: "aws_sdk_iotsitewise.types.asset_hierarchies.AssetHierarchies"
    """<p>A list of asset hierarchies that each contain a <code>hierarchyId</code>. A hierarchy specifies allowed parent/child asset relationships.</p>"""
    description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>A description for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedAssetsSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["assetModelId"] = value["asset_model_id"]
    import aws_sdk_iotsitewise.types.timestamp

    out["creationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["lastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import aws_sdk_iotsitewise.types.asset_status

    out["status"] = aws_sdk_iotsitewise.types.asset_status.serialize_json(
        value["status"]
    )
    import aws_sdk_iotsitewise.types.asset_hierarchies

    out["hierarchies"] = aws_sdk_iotsitewise.types.asset_hierarchies.serialize_json(
        value["hierarchies"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AssociatedAssetsSummary:
    out: AssociatedAssetsSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssociatedAssetsSummary.id required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssociatedAssetsSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssociatedAssetsSummary.name required")
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("AssociatedAssetsSummary.asset_model_id required")
    if "creationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["creation_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("AssociatedAssetsSummary.creation_date required")
    if "lastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["last_update_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("AssociatedAssetsSummary.last_update_date required")
    if "status" in data:
        import aws_sdk_iotsitewise.types.asset_status

        out["status"] = aws_sdk_iotsitewise.types.asset_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AssociatedAssetsSummary.status required")
    if "hierarchies" in data:
        import aws_sdk_iotsitewise.types.asset_hierarchies

        out["hierarchies"] = (
            aws_sdk_iotsitewise.types.asset_hierarchies.deserialize_json(
                data["hierarchies"]
            )
        )
    else:
        raise DeserializationError("AssociatedAssetsSummary.hierarchies required")
    if "description" in data:
        out["description"] = data["description"]
    return out
