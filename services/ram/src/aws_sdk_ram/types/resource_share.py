"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShare``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.resource_share_configuration
    import aws_sdk_ram.types.resource_share_feature_set
    import aws_sdk_ram.types.resource_share_status
    import aws_sdk_ram.types.string
    import aws_sdk_ram.types.tag_list


class ResourceShare(TypedDict):
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share</p>"""
    name: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The name of the resource share.</p>"""
    owning_account_id: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource share.</p>"""
    allow_external_principals: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>Indicates whether principals outside your organization in Organizations can be associated with a resource share.</p> <ul> <li> <p> <code>True</code> – the resource share can be shared with any Amazon Web Services account.</p> </li> <li> <p> <code>False</code> – the resource share can be shared with only accounts in the same organization as the account that owns the resource share.</p> </li> </ul>"""
    status: NotRequired["aws_sdk_ram.types.resource_share_status.ResourceShareStatus"]
    """<p>The current status of the resource share.</p>"""
    status_message: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>A message about the status of the resource share.</p>"""
    tags: NotRequired["aws_sdk_ram.types.tag_list.TagList"]
    """<p>The tag key and value pairs attached to the resource share.</p>"""
    creation_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the resource share was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the resource share was last updated.</p>"""
    feature_set: NotRequired[
        "aws_sdk_ram.types.resource_share_feature_set.ResourceShareFeatureSet"
    ]
    """<p>Indicates what features are available for this resource share. This parameter can have one of the following values:</p> <ul> <li> <p> <b>STANDARD</b> – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in RAM using the console or APIs. This resource share might have been created by RAM, or it might have been <b>CREATED_FROM_POLICY</b> and then promoted.</p> </li> <li> <p> <b>CREATED_FROM_POLICY</b> – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the Amazon Web Services account that created it. You can't modify it in RAM unless you promote it. For more information, see <a>PromoteResourceShareCreatedFromPolicy</a>.</p> </li> <li> <p> <b>PROMOTING_TO_STANDARD</b> – This resource share was originally <code>CREATED_FROM_POLICY</code>, but the customer ran the <a>PromoteResourceShareCreatedFromPolicy</a> and that operation is still in progress. This value changes to <code>STANDARD</code> when complete.</p> </li> </ul>"""
    resource_share_configuration: NotRequired[
        "aws_sdk_ram.types.resource_share_configuration.ResourceShareConfiguration"
    ]
    """<p>The configuration of the resource share</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShare) -> dict:
    out: dict = {}
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "owning_account_id" in value:
        out["owningAccountId"] = value["owning_account_id"]
    if "allow_external_principals" in value:
        out["allowExternalPrincipals"] = value["allow_external_principals"]
    if "status" in value:
        import aws_sdk_ram.types.resource_share_status

        out["status"] = aws_sdk_ram.types.resource_share_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "tags" in value:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.serialize_json(value["tags"])
    if "creation_time" in value:
        import aws_sdk_ram.types.date_time

        out["creationTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_ram.types.date_time

        out["lastUpdatedTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "feature_set" in value:
        import aws_sdk_ram.types.resource_share_feature_set

        out["featureSet"] = aws_sdk_ram.types.resource_share_feature_set.serialize_json(
            value["feature_set"]
        )
    if "resource_share_configuration" in value:
        import aws_sdk_ram.types.resource_share_configuration

        out["resourceShareConfiguration"] = (
            aws_sdk_ram.types.resource_share_configuration.serialize_json(
                value["resource_share_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceShare:
    out: ResourceShare = {}  # type: ignore[typeddict-item]
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "owningAccountId" in data:
        out["owning_account_id"] = data["owningAccountId"]
    if "allowExternalPrincipals" in data:
        out["allow_external_principals"] = data["allowExternalPrincipals"]
    if "status" in data:
        import aws_sdk_ram.types.resource_share_status

        out["status"] = aws_sdk_ram.types.resource_share_status.deserialize_json(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "tags" in data:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.deserialize_json(data["tags"])
    if "creationTime" in data:
        import aws_sdk_ram.types.date_time

        out["creation_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_ram.types.date_time

        out["last_updated_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "featureSet" in data:
        import aws_sdk_ram.types.resource_share_feature_set

        out["feature_set"] = (
            aws_sdk_ram.types.resource_share_feature_set.deserialize_json(
                data["featureSet"]
            )
        )
    if "resourceShareConfiguration" in data:
        import aws_sdk_ram.types.resource_share_configuration

        out["resource_share_configuration"] = (
            aws_sdk_ram.types.resource_share_configuration.deserialize_json(
                data["resourceShareConfiguration"]
            )
        )
    return out
