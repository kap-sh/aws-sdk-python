"""Generated from Smithy shape ``com.amazonaws.ec2#CreateImageUsageReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateImageUsageReportRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "resource_types" in value:
        import aws_sdk_ec2.types.image_usage_resource_type_request_list

        aws_sdk_ec2.types.image_usage_resource_type_request_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{prefix}.ResourceTypes"
        )
    if "account_ids" in value:
        import aws_sdk_ec2.types.image_usage_report_user_id_string_list

        aws_sdk_ec2.types.image_usage_report_user_id_string_list.serialize_ec2_query(
            value["account_ids"], pairs, f"{prefix}.AccountIds"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateImageUsageReportRequest:
    out: CreateImageUsageReportRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ResourceTypes") is not None:
        import aws_sdk_ec2.types.image_usage_resource_type_request_list

        out["resource_types"] = (
            aws_sdk_ec2.types.image_usage_resource_type_request_list.deserialize_ec2_query(
                el, "ResourceTypes"
            )
        )
    if el.find("AccountIds") is not None:
        import aws_sdk_ec2.types.image_usage_report_user_id_string_list

        out["account_ids"] = (
            aws_sdk_ec2.types.image_usage_report_user_id_string_list.deserialize_ec2_query(
                el, "AccountIds"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
