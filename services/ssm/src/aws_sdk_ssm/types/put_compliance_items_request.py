"""Generated from Smithy shape ``com.amazonaws.ssm#PutComplianceItemsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_execution_summary
    import aws_sdk_ssm.types.compliance_item_content_hash
    import aws_sdk_ssm.types.compliance_item_entry_list
    import aws_sdk_ssm.types.compliance_resource_id
    import aws_sdk_ssm.types.compliance_resource_type
    import aws_sdk_ssm.types.compliance_type_name
    import aws_sdk_ssm.types.compliance_upload_type


class PutComplianceItemsRequest(TypedDict):
    resource_id: "aws_sdk_ssm.types.compliance_resource_id.ComplianceResourceId"
    """<p>Specify an ID for this resource. For a managed node, this is the node ID.</p>"""
    resource_type: "aws_sdk_ssm.types.compliance_resource_type.ComplianceResourceType"
    """<p>Specify the type of resource. <code>ManagedInstance</code> is currently the only supported resource type.</p>"""
    compliance_type: "aws_sdk_ssm.types.compliance_type_name.ComplianceTypeName"
    """<p>Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:<code>string</code>.</p>"""
    execution_summary: (
        "aws_sdk_ssm.types.compliance_execution_summary.ComplianceExecutionSummary"
    )
    """<p>A summary of the call execution that includes an execution ID, the type of execution (for example, <code>Command</code>), and the date/time of the execution using a datetime object that is saved in the following format: <code>yyyy-MM-dd'T'HH:mm:ss'Z'</code> </p>"""
    items: "aws_sdk_ssm.types.compliance_item_entry_list.ComplianceItemEntryList"
    """<p>Information about the compliance as defined by the resource type. For example, for a patch compliance type, <code>Items</code> includes information about the PatchSeverity, Classification, and so on.</p>"""
    item_content_hash: NotRequired[
        "aws_sdk_ssm.types.compliance_item_content_hash.ComplianceItemContentHash"
    ]
    """<p>MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.</p>"""
    upload_type: NotRequired[
        "aws_sdk_ssm.types.compliance_upload_type.ComplianceUploadType"
    ]
    """<p>The mode for uploading compliance items. You can specify <code>COMPLETE</code> or <code>PARTIAL</code>. In <code>COMPLETE</code> mode, the system overwrites all existing compliance information for the resource. You must provide a full list of compliance items each time you send the request.</p> <p>In <code>PARTIAL</code> mode, the system overwrites compliance information for a specific association. The association must be configured with <code>SyncCompliance</code> set to <code>MANUAL</code>. By default, all requests use <code>COMPLETE</code> mode.</p> <note> <p>This attribute is only valid for association compliance.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutComplianceItemsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    out["ComplianceType"] = value["compliance_type"]
    import aws_sdk_ssm.types.compliance_execution_summary

    out["ExecutionSummary"] = (
        aws_sdk_ssm.types.compliance_execution_summary.serialize_aws_json_1_1(
            value["execution_summary"]
        )
    )
    import aws_sdk_ssm.types.compliance_item_entry_list

    out["Items"] = aws_sdk_ssm.types.compliance_item_entry_list.serialize_aws_json_1_1(
        value["items"]
    )
    if "item_content_hash" in value:
        out["ItemContentHash"] = value["item_content_hash"]
    if "upload_type" in value:
        import aws_sdk_ssm.types.compliance_upload_type

        out["UploadType"] = (
            aws_sdk_ssm.types.compliance_upload_type.serialize_aws_json_1_1(
                value["upload_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutComplianceItemsRequest:
    out: PutComplianceItemsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("PutComplianceItemsRequest.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("PutComplianceItemsRequest.resource_type required")
    if "ComplianceType" in data:
        out["compliance_type"] = data["ComplianceType"]
    else:
        raise DeserializationError("PutComplianceItemsRequest.compliance_type required")
    if "ExecutionSummary" in data:
        import aws_sdk_ssm.types.compliance_execution_summary

        out["execution_summary"] = (
            aws_sdk_ssm.types.compliance_execution_summary.deserialize_aws_json_1_1(
                data["ExecutionSummary"]
            )
        )
    else:
        raise DeserializationError(
            "PutComplianceItemsRequest.execution_summary required"
        )
    if "Items" in data:
        import aws_sdk_ssm.types.compliance_item_entry_list

        out["items"] = (
            aws_sdk_ssm.types.compliance_item_entry_list.deserialize_aws_json_1_1(
                data["Items"]
            )
        )
    else:
        raise DeserializationError("PutComplianceItemsRequest.items required")
    if "ItemContentHash" in data:
        out["item_content_hash"] = data["ItemContentHash"]
    if "UploadType" in data:
        import aws_sdk_ssm.types.compliance_upload_type

        out["upload_type"] = (
            aws_sdk_ssm.types.compliance_upload_type.deserialize_aws_json_1_1(
                data["UploadType"]
            )
        )
    return out
