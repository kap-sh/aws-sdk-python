"""Generated from Smithy shape ``com.amazonaws.ec2#CreateImageUsageReportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_image_usage_report_client_token
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_usage_report_user_id_string_list
    import aws_sdk_ec2.types.image_usage_resource_type_request_list
    import aws_sdk_ec2.types.tag_specification_list


class CreateImageUsageReportRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image to report on.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resource_types: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_request_list.ImageUsageResourceTypeRequestList"
    ]
    """<p>The resource types to include in the report.</p>"""
    account_ids: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_user_id_string_list.ImageUsageReportUserIdStringList"
    ]
    """<p>The Amazon Web Services account IDs to include in the report. To include all accounts, omit this parameter.</p>"""
    client_token: NotRequired[
        "aws_sdk_ec2.types.create_image_usage_report_client_token.CreateImageUsageReportClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the report on creation. The <code>ResourceType</code> must be set to <code>image-usage-report</code>; any other value will cause the report creation to fail.</p> <p>To tag a report after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>"""
