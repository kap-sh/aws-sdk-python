"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#System``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.organization_id
    import aws_sdk_resiliencehubv2.types.ou_id
    import aws_sdk_resiliencehubv2.types.system_id
    import aws_sdk_resiliencehubv2.types.tag_map


class System(TypedDict):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    system_id: "aws_sdk_resiliencehubv2.types.system_id.SystemId"
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    sharing_enabled: NotRequired["bool"]
    """<p>Indicates whether cross-account sharing is enabled.</p>"""
    tags: NotRequired["aws_sdk_resiliencehubv2.types.tag_map.TagMap"]
    kms_key_id: NotRequired["aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    organization_id: NotRequired[
        "aws_sdk_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>The AWS Organizations identifier for the system.</p>"""
    ou_id: NotRequired["aws_sdk_resiliencehubv2.types.ou_id.OuId"]
    """<p>The organizational unit (OU) identifier for the system.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: System) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["systemId"] = value["system_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    if "tags" in value:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.serialize_json(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "ou_id" in value:
        out["ouId"] = value["ou_id"]
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> System:
    out: System = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("System.system_arn required")
    if "systemId" in data:
        out["system_id"] = data["systemId"]
    else:
        raise DeserializationError("System.system_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("System.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "sharingEnabled" in data:
        out["sharing_enabled"] = data["sharingEnabled"]
    if "tags" in data:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    if "ouId" in data:
        out["ou_id"] = data["ouId"]
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
