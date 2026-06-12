"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateTenantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.sending_status
    import aws_sdk_sesv2.types.tag_list
    import aws_sdk_sesv2.types.tenant_id
    import aws_sdk_sesv2.types.tenant_name
    import aws_sdk_sesv2.types.tenant_suppression_attributes
    import aws_sdk_sesv2.types.timestamp


class CreateTenantResponse(TypedDict):
    tenant_name: NotRequired["aws_sdk_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant.</p>"""
    tenant_id: NotRequired["aws_sdk_sesv2.types.tenant_id.TenantId"]
    """<p>A unique identifier for the tenant.</p>"""
    tenant_arn: NotRequired[
        "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the tenant.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the tenant was created.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) associated with the tenant.</p>"""
    sending_status: NotRequired["aws_sdk_sesv2.types.sending_status.SendingStatus"]
    """<p>The status of email sending capability for the tenant.</p>"""
    suppression_attributes: NotRequired[
        "aws_sdk_sesv2.types.tenant_suppression_attributes.TenantSuppressionAttributes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTenantResponse) -> dict:
    out: dict = {}
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "tenant_arn" in value:
        out["TenantArn"] = value["tenant_arn"]
    if "created_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CreatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    if "sending_status" in value:
        import aws_sdk_sesv2.types.sending_status

        out["SendingStatus"] = aws_sdk_sesv2.types.sending_status.serialize_json(
            value["sending_status"]
        )
    if "suppression_attributes" in value:
        import aws_sdk_sesv2.types.tenant_suppression_attributes

        out["SuppressionAttributes"] = (
            aws_sdk_sesv2.types.tenant_suppression_attributes.serialize_json(
                value["suppression_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTenantResponse:
    out: CreateTenantResponse = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    if "TenantId" in data:
        out["tenant_id"] = data["TenantId"]
    if "TenantArn" in data:
        out["tenant_arn"] = data["TenantArn"]
    if "CreatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["created_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "SendingStatus" in data:
        import aws_sdk_sesv2.types.sending_status

        out["sending_status"] = aws_sdk_sesv2.types.sending_status.deserialize_json(
            data["SendingStatus"]
        )
    if "SuppressionAttributes" in data:
        import aws_sdk_sesv2.types.tenant_suppression_attributes

        out["suppression_attributes"] = (
            aws_sdk_sesv2.types.tenant_suppression_attributes.deserialize_json(
                data["SuppressionAttributes"]
            )
        )
    return out
