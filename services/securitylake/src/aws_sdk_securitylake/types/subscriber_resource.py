"""Generated from Smithy shape ``com.amazonaws.securitylake#SubscriberResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securitylake.types.access_type_list
    import aws_sdk_securitylake.types.amazon_resource_name
    import aws_sdk_securitylake.types.aws_identity
    import aws_sdk_securitylake.types.log_source_resource_list
    import aws_sdk_securitylake.types.resource_share_arn
    import aws_sdk_securitylake.types.resource_share_name
    import aws_sdk_securitylake.types.role_arn
    import aws_sdk_securitylake.types.s3_bucket_arn
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.subscriber_status
    import aws_sdk_securitylake.types.uuid


class SubscriberResource(TypedDict, closed=True):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>The subscriber ID of the Amazon Security Lake subscriber account.</p>"""
    subscriber_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The subscriber ARN of the Amazon Security Lake subscriber account.</p>"""
    subscriber_identity: "aws_sdk_securitylake.types.aws_identity.AwsIdentity"
    """<p>The Amazon Web Services identity used to access your data.</p>"""
    subscriber_name: "aws_sdk_securitylake.types.safe_string.SafeString"
    """<p>The name of your Amazon Security Lake subscriber account.</p>"""
    subscriber_description: NotRequired[
        "aws_sdk_securitylake.types.safe_string.SafeString"
    ]
    """<p>The subscriber descriptions for a subscriber account. The description for a subscriber includes <code>subscriberName</code>, <code>accountID</code>, <code>externalID</code>, and <code>subscriberId</code>.</p>"""
    sources: "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList"
    r"""<p>Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services. For more information, see the <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html\">Amazon Security Lake User Guide</a>.</p>"""
    access_types: NotRequired[
        "aws_sdk_securitylake.types.access_type_list.AccessTypeList"
    ]
    """<p>You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.</p> <p> Subscribers can consume data by directly querying Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as <code>LAKEFORMATION</code>.</p>"""
    role_arn: NotRequired["aws_sdk_securitylake.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) specifying the role of the subscriber.</p>"""
    s3_bucket_arn: NotRequired["aws_sdk_securitylake.types.s3_bucket_arn.S3BucketArn"]
    """<p>The ARN for the Amazon S3 bucket.</p>"""
    subscriber_endpoint: NotRequired[
        "aws_sdk_securitylake.types.safe_string.SafeString"
    ]
    """<p>The subscriber endpoint to which exception messages are posted.</p>"""
    subscriber_status: NotRequired[
        "aws_sdk_securitylake.types.subscriber_status.SubscriberStatus"
    ]
    """<p>The subscriber status of the Amazon Security Lake subscriber account.</p>"""
    resource_share_arn: NotRequired[
        "aws_sdk_securitylake.types.resource_share_arn.ResourceShareArn"
    ]
    """<p>The Amazon Resource Name (ARN) which uniquely defines the Amazon Web Services RAM resource share. Before accepting the RAM resource share invitation, you can view details related to the RAM resource share.</p> <p>This field is available only for Lake Formation subscribers created after March 8, 2023.</p>"""
    resource_share_name: NotRequired[
        "aws_sdk_securitylake.types.resource_share_name.ResourceShareName"
    ]
    """<p>The name of the resource share.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the subscriber was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the subscriber was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriberResource) -> dict:
    out: dict = {}
    out["subscriberId"] = value["subscriber_id"]
    out["subscriberArn"] = value["subscriber_arn"]
    import aws_sdk_securitylake.types.aws_identity

    out["subscriberIdentity"] = aws_sdk_securitylake.types.aws_identity.serialize_json(
        value["subscriber_identity"]
    )
    out["subscriberName"] = value["subscriber_name"]
    if "subscriber_description" in value:
        out["subscriberDescription"] = value["subscriber_description"]
    import aws_sdk_securitylake.types.log_source_resource_list

    out["sources"] = aws_sdk_securitylake.types.log_source_resource_list.serialize_json(
        value["sources"]
    )
    if "access_types" in value:
        import aws_sdk_securitylake.types.access_type_list

        out["accessTypes"] = aws_sdk_securitylake.types.access_type_list.serialize_json(
            value["access_types"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "s3_bucket_arn" in value:
        out["s3BucketArn"] = value["s3_bucket_arn"]
    if "subscriber_endpoint" in value:
        out["subscriberEndpoint"] = value["subscriber_endpoint"]
    if "subscriber_status" in value:
        import aws_sdk_securitylake.types.subscriber_status

        out["subscriberStatus"] = (
            aws_sdk_securitylake.types.subscriber_status.serialize_json(
                value["subscriber_status"]
            )
        )
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "resource_share_name" in value:
        out["resourceShareName"] = value["resource_share_name"]
    if "created_at" in value:
        import aws_sdk_securitylake.types._prelude.timestamp

        out["createdAt"] = aws_sdk_securitylake.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_securitylake.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_securitylake.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> SubscriberResource:
    out: SubscriberResource = {}  # type: ignore[typeddict-item]
    if "subscriberId" in data:
        out["subscriber_id"] = data["subscriberId"]
    else:
        raise DeserializationError("SubscriberResource.subscriber_id required")
    if "subscriberArn" in data:
        out["subscriber_arn"] = data["subscriberArn"]
    else:
        raise DeserializationError("SubscriberResource.subscriber_arn required")
    if "subscriberIdentity" in data:
        import aws_sdk_securitylake.types.aws_identity

        out["subscriber_identity"] = (
            aws_sdk_securitylake.types.aws_identity.deserialize_json(
                data["subscriberIdentity"]
            )
        )
    else:
        raise DeserializationError("SubscriberResource.subscriber_identity required")
    if "subscriberName" in data:
        out["subscriber_name"] = data["subscriberName"]
    else:
        raise DeserializationError("SubscriberResource.subscriber_name required")
    if "subscriberDescription" in data:
        out["subscriber_description"] = data["subscriberDescription"]
    if "sources" in data:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("SubscriberResource.sources required")
    if "accessTypes" in data:
        import aws_sdk_securitylake.types.access_type_list

        out["access_types"] = (
            aws_sdk_securitylake.types.access_type_list.deserialize_json(
                data["accessTypes"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "s3BucketArn" in data:
        out["s3_bucket_arn"] = data["s3BucketArn"]
    if "subscriberEndpoint" in data:
        out["subscriber_endpoint"] = data["subscriberEndpoint"]
    if "subscriberStatus" in data:
        import aws_sdk_securitylake.types.subscriber_status

        out["subscriber_status"] = (
            aws_sdk_securitylake.types.subscriber_status.deserialize_json(
                data["subscriberStatus"]
            )
        )
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "resourceShareName" in data:
        out["resource_share_name"] = data["resourceShareName"]
    if "createdAt" in data:
        import aws_sdk_securitylake.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securitylake.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_securitylake.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_securitylake.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
