"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.associated_system_list
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.tag_map


class ImportAppRequest(TypedDict):
    v1_app_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    policy_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    kms_key_id: NotRequired["aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    skip_manually_added_resources: NotRequired["bool"]
    """<p>Whether to skip manually added resources during import.</p>"""
    associated_systems: NotRequired[
        "aws_sdk_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
    ]
    """<p>The systems to associate with the imported service.</p>"""
    tags: NotRequired["aws_sdk_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportAppRequest) -> dict:
    out: dict = {}
    out["v1AppArn"] = value["v1_app_arn"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "skip_manually_added_resources" in value:
        out["skipManuallyAddedResources"] = value["skip_manually_added_resources"]
    if "associated_systems" in value:
        import aws_sdk_resiliencehubv2.types.associated_system_list

        out["associatedSystems"] = (
            aws_sdk_resiliencehubv2.types.associated_system_list.serialize_json(
                value["associated_systems"]
            )
        )
    if "tags" in value:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportAppRequest:
    out: ImportAppRequest = {}  # type: ignore[typeddict-item]
    if "v1AppArn" in data:
        out["v1_app_arn"] = data["v1AppArn"]
    else:
        raise DeserializationError("ImportAppRequest.v1_app_arn required")
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "skipManuallyAddedResources" in data:
        out["skip_manually_added_resources"] = data["skipManuallyAddedResources"]
    if "associatedSystems" in data:
        import aws_sdk_resiliencehubv2.types.associated_system_list

        out["associated_systems"] = (
            aws_sdk_resiliencehubv2.types.associated_system_list.deserialize_json(
                data["associatedSystems"]
            )
        )
    if "tags" in data:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
