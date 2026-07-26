"""Generated from Smithy shape ``com.amazonaws.sagemaker#Workteam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.member_definitions
    import capo_sagemaker.types.notification_configuration
    import capo_sagemaker.types.product_listings
    import capo_sagemaker.types.string
    import capo_sagemaker.types.string200
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.worker_access_configuration
    import capo_sagemaker.types.workforce_arn
    import capo_sagemaker.types.workteam_arn
    import capo_sagemaker.types.workteam_name


class Workteam(TypedDict, closed=True):
    workteam_name: NotRequired["capo_sagemaker.types.workteam_name.WorkteamName"]
    """<p>The name of the work team.</p>"""
    member_definitions: NotRequired[
        "capo_sagemaker.types.member_definitions.MemberDefinitions"
    ]
    """<p>A list of <code>MemberDefinition</code> objects that contains objects that identify the workers that make up the work team. </p> <p>Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use <code>CognitoMemberDefinition</code>. For workforces created using your own OIDC identity provider (IdP) use <code>OidcMemberDefinition</code>.</p>"""
    workteam_arn: NotRequired["capo_sagemaker.types.workteam_arn.WorkteamArn"]
    """<p>The Amazon Resource Name (ARN) that identifies the work team.</p>"""
    workforce_arn: NotRequired["capo_sagemaker.types.workforce_arn.WorkforceArn"]
    """<p>The Amazon Resource Name (ARN) of the workforce.</p>"""
    product_listing_ids: NotRequired[
        "capo_sagemaker.types.product_listings.ProductListings"
    ]
    """<p>The Amazon Marketplace identifier for a vendor's work team.</p>"""
    description: NotRequired["capo_sagemaker.types.string200.String200"]
    """<p>A description of the work team.</p>"""
    sub_domain: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The URI of the labeling job's user interface. Workers open this URI to start labeling your data objects.</p>"""
    create_date: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the work team was created (timestamp).</p>"""
    last_updated_date: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the work team was last updated (timestamp).</p>"""
    notification_configuration: NotRequired[
        "capo_sagemaker.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>Configures SNS notifications of available or expiring work items for work teams.</p>"""
    worker_access_configuration: NotRequired[
        "capo_sagemaker.types.worker_access_configuration.WorkerAccessConfiguration"
    ]
    """<p>Describes any access constraints that have been defined for Amazon S3 resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workteam) -> dict:
    out: dict = {}
    if "workteam_name" in value:
        out["WorkteamName"] = value["workteam_name"]
    if "member_definitions" in value:
        import capo_sagemaker.types.member_definitions

        out["MemberDefinitions"] = (
            capo_sagemaker.types.member_definitions.serialize_aws_json_1_1(
                value["member_definitions"]
            )
        )
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    if "workforce_arn" in value:
        out["WorkforceArn"] = value["workforce_arn"]
    if "product_listing_ids" in value:
        import capo_sagemaker.types.product_listings

        out["ProductListingIds"] = (
            capo_sagemaker.types.product_listings.serialize_aws_json_1_1(
                value["product_listing_ids"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "sub_domain" in value:
        out["SubDomain"] = value["sub_domain"]
    if "create_date" in value:
        import capo_sagemaker.types.timestamp

        out["CreateDate"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["create_date"]
        )
    if "last_updated_date" in value:
        import capo_sagemaker.types.timestamp

        out["LastUpdatedDate"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_date"]
        )
    if "notification_configuration" in value:
        import capo_sagemaker.types.notification_configuration

        out["NotificationConfiguration"] = (
            capo_sagemaker.types.notification_configuration.serialize_aws_json_1_1(
                value["notification_configuration"]
            )
        )
    if "worker_access_configuration" in value:
        import capo_sagemaker.types.worker_access_configuration

        out["WorkerAccessConfiguration"] = (
            capo_sagemaker.types.worker_access_configuration.serialize_aws_json_1_1(
                value["worker_access_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Workteam:
    out: Workteam = {}  # type: ignore[typeddict-item]
    if "WorkteamName" in data:
        out["workteam_name"] = data["WorkteamName"]
    if "MemberDefinitions" in data:
        import capo_sagemaker.types.member_definitions

        out["member_definitions"] = (
            capo_sagemaker.types.member_definitions.deserialize_aws_json_1_1(
                data["MemberDefinitions"]
            )
        )
    if "WorkteamArn" in data:
        out["workteam_arn"] = data["WorkteamArn"]
    if "WorkforceArn" in data:
        out["workforce_arn"] = data["WorkforceArn"]
    if "ProductListingIds" in data:
        import capo_sagemaker.types.product_listings

        out["product_listing_ids"] = (
            capo_sagemaker.types.product_listings.deserialize_aws_json_1_1(
                data["ProductListingIds"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "SubDomain" in data:
        out["sub_domain"] = data["SubDomain"]
    if "CreateDate" in data:
        import capo_sagemaker.types.timestamp

        out["create_date"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreateDate"]
        )
    if "LastUpdatedDate" in data:
        import capo_sagemaker.types.timestamp

        out["last_updated_date"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedDate"]
            )
        )
    if "NotificationConfiguration" in data:
        import capo_sagemaker.types.notification_configuration

        out["notification_configuration"] = (
            capo_sagemaker.types.notification_configuration.deserialize_aws_json_1_1(
                data["NotificationConfiguration"]
            )
        )
    if "WorkerAccessConfiguration" in data:
        import capo_sagemaker.types.worker_access_configuration

        out["worker_access_configuration"] = (
            capo_sagemaker.types.worker_access_configuration.deserialize_aws_json_1_1(
                data["WorkerAccessConfiguration"]
            )
        )
    return out
