"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesFindingFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.date_filter_list
    import aws_sdk_securityhub.types.map_filter_list
    import aws_sdk_securityhub.types.number_filter_list
    import aws_sdk_securityhub.types.string_filter_list


class AutomationRulesFindingFilters(TypedDict):
    product_arn: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub CSPM. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    aws_account_id: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The Amazon Web Services account ID in which a finding was generated.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    id: NotRequired["aws_sdk_securityhub.types.string_filter_list.StringFilterList"]
    """<p> The product-specific identifier for a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    generator_id: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The identifier for the solution-specific component that generated a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    type: NotRequired["aws_sdk_securityhub.types.string_filter_list.StringFilterList"]
    r"""<p> One or more finding types in the format of namespace/category/classifier that classify a finding. For a list of namespaces, classifiers, and categories, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html\">Types taxonomy for ASFF</a> in the <i>Security Hub CSPM User Guide</i>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    first_observed_at: NotRequired[
        "aws_sdk_securityhub.types.date_filter_list.DateFilterList"
    ]
    r"""<p> A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    last_observed_at: NotRequired[
        "aws_sdk_securityhub.types.date_filter_list.DateFilterList"
    ]
    r"""<p> A timestamp that indicates when the security findings provider most recently observed a change in the resource that is involved in the finding. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.date_filter_list.DateFilterList"]
    r"""<p> A timestamp that indicates when this finding record was created. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.date_filter_list.DateFilterList"]
    r"""<p> A timestamp that indicates when the finding record was most recently updated. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    confidence: NotRequired[
        "aws_sdk_securityhub.types.number_filter_list.NumberFilterList"
    ]
    r"""<p>The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. <code>Confidence</code> is scored on a 0–100 basis using a ratio scale. A value of <code>0</code> means 0 percent confidence, and a value of <code>100</code> means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasn't been verified. For more information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence\">Confidence</a> in the <i>Security Hub CSPM User Guide</i>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    criticality: NotRequired[
        "aws_sdk_securityhub.types.number_filter_list.NumberFilterList"
    ]
    r"""<p> The level of importance that is assigned to the resources that are associated with a finding. <code>Criticality</code> is scored on a 0–100 basis, using a ratio scale that supports only full integers. A score of <code>0</code> means that the underlying resources have no criticality, and a score of <code>100</code> is reserved for the most critical resources. For more information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality\">Criticality</a> in the <i>Security Hub CSPM User Guide</i>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    title: NotRequired["aws_sdk_securityhub.types.string_filter_list.StringFilterList"]
    """<p> A finding's title. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> A finding's description. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    source_url: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides a URL that links to a page about the current finding in the finding product. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    product_name: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub CSPM. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    company_name: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The name of the company for the product that generated the finding. For control-based findings, the company is Amazon Web Services. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    severity_label: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The severity value of the finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_type: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The type of resource that the finding pertains to. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_id: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The identifier for the given resource type. For Amazon Web Services resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For Amazon Web Services resources that lack ARNs, this is the identifier as defined by the Amazon Web Services service that created the resource. For non-Amazon Web Services resources, this is a unique identifier that is associated with the resource. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 100 items. </p>"""
    resource_partition: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The partition in which the resource that the finding pertains to is located. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_region: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The Amazon Web Services Region where the resource that a finding pertains to is located. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_tags: NotRequired[
        "aws_sdk_securityhub.types.map_filter_list.MapFilterList"
    ]
    """<p> A list of Amazon Web Services tags associated with a resource at the time the finding was processed. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_details_other: NotRequired[
        "aws_sdk_securityhub.types.map_filter_list.MapFilterList"
    ]
    """<p> Custom fields and values about the resource that a finding pertains to. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    compliance_status: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The result of a security check. This field is only used for findings generated from controls. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    compliance_security_control_id: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The security control ID for which a finding was generated. Security control IDs are the same across standards.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    compliance_associated_standards_id: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    r"""<p>The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html\">DescribeStandards</a> API response.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    verification_state: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides the veracity of a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    workflow_status: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides information about the status of the investigation into a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    record_state: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> Provides the current state of a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    related_findings_product_arn: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The ARN for the product that generated a related finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    related_findings_id: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The product-generated identifier for a related finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    note_text: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The text of a user-defined note that's added to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    note_updated_at: NotRequired[
        "aws_sdk_securityhub.types.date_filter_list.DateFilterList"
    ]
    r"""<p> The timestamp of when the note was updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    note_updated_by: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The principal that created a note. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    user_defined_fields: NotRequired[
        "aws_sdk_securityhub.types.map_filter_list.MapFilterList"
    ]
    """<p> A list of user-defined name and value string pairs added to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_application_arn: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The Amazon Resource Name (ARN) of the application that is related to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    resource_application_name: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p> The name of the application that is related to a finding. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""
    aws_account_name: NotRequired[
        "aws_sdk_securityhub.types.string_filter_list.StringFilterList"
    ]
    """<p>The name of the Amazon Web Services account in which a finding was generated. </p> <p> Array Members: Minimum number of 1 item. Maximum number of 20 items. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesFindingFilters) -> dict:
    out: dict = {}
    if "product_arn" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ProductArn"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["product_arn"]
        )
    if "aws_account_id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["AwsAccountId"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["aws_account_id"]
            )
        )
    if "id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["Id"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["id"]
        )
    if "generator_id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["GeneratorId"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["generator_id"]
            )
        )
    if "type" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["Type"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["type"]
        )
    if "first_observed_at" in value:
        import aws_sdk_securityhub.types.date_filter_list

        out["FirstObservedAt"] = (
            aws_sdk_securityhub.types.date_filter_list.serialize_json(
                value["first_observed_at"]
            )
        )
    if "last_observed_at" in value:
        import aws_sdk_securityhub.types.date_filter_list

        out["LastObservedAt"] = (
            aws_sdk_securityhub.types.date_filter_list.serialize_json(
                value["last_observed_at"]
            )
        )
    if "created_at" in value:
        import aws_sdk_securityhub.types.date_filter_list

        out["CreatedAt"] = aws_sdk_securityhub.types.date_filter_list.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_securityhub.types.date_filter_list

        out["UpdatedAt"] = aws_sdk_securityhub.types.date_filter_list.serialize_json(
            value["updated_at"]
        )
    if "confidence" in value:
        import aws_sdk_securityhub.types.number_filter_list

        out["Confidence"] = aws_sdk_securityhub.types.number_filter_list.serialize_json(
            value["confidence"]
        )
    if "criticality" in value:
        import aws_sdk_securityhub.types.number_filter_list

        out["Criticality"] = (
            aws_sdk_securityhub.types.number_filter_list.serialize_json(
                value["criticality"]
            )
        )
    if "title" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["Title"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["title"]
        )
    if "description" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["Description"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["description"]
            )
        )
    if "source_url" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["SourceUrl"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["source_url"]
        )
    if "product_name" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ProductName"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["product_name"]
            )
        )
    if "company_name" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["CompanyName"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["company_name"]
            )
        )
    if "severity_label" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["SeverityLabel"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["severity_label"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ResourceType"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ResourceId"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["resource_id"]
        )
    if "resource_partition" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ResourcePartition"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["resource_partition"]
            )
        )
    if "resource_region" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ResourceRegion"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["resource_region"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_securityhub.types.map_filter_list

        out["ResourceTags"] = aws_sdk_securityhub.types.map_filter_list.serialize_json(
            value["resource_tags"]
        )
    if "resource_details_other" in value:
        import aws_sdk_securityhub.types.map_filter_list

        out["ResourceDetailsOther"] = (
            aws_sdk_securityhub.types.map_filter_list.serialize_json(
                value["resource_details_other"]
            )
        )
    if "compliance_status" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ComplianceStatus"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["compliance_status"]
            )
        )
    if "compliance_security_control_id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ComplianceSecurityControlId"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["compliance_security_control_id"]
            )
        )
    if "compliance_associated_standards_id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ComplianceAssociatedStandardsId"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["compliance_associated_standards_id"]
            )
        )
    if "verification_state" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["VerificationState"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["verification_state"]
            )
        )
    if "workflow_status" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["WorkflowStatus"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["workflow_status"]
            )
        )
    if "record_state" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["RecordState"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["record_state"]
            )
        )
    if "related_findings_product_arn" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["RelatedFindingsProductArn"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["related_findings_product_arn"]
            )
        )
    if "related_findings_id" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["RelatedFindingsId"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["related_findings_id"]
            )
        )
    if "note_text" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["NoteText"] = aws_sdk_securityhub.types.string_filter_list.serialize_json(
            value["note_text"]
        )
    if "note_updated_at" in value:
        import aws_sdk_securityhub.types.date_filter_list

        out["NoteUpdatedAt"] = (
            aws_sdk_securityhub.types.date_filter_list.serialize_json(
                value["note_updated_at"]
            )
        )
    if "note_updated_by" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["NoteUpdatedBy"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["note_updated_by"]
            )
        )
    if "user_defined_fields" in value:
        import aws_sdk_securityhub.types.map_filter_list

        out["UserDefinedFields"] = (
            aws_sdk_securityhub.types.map_filter_list.serialize_json(
                value["user_defined_fields"]
            )
        )
    if "resource_application_arn" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ResourceApplicationArn"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["resource_application_arn"]
            )
        )
    if "resource_application_name" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["ResourceApplicationName"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["resource_application_name"]
            )
        )
    if "aws_account_name" in value:
        import aws_sdk_securityhub.types.string_filter_list

        out["AwsAccountName"] = (
            aws_sdk_securityhub.types.string_filter_list.serialize_json(
                value["aws_account_name"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesFindingFilters:
    out: AutomationRulesFindingFilters = {}  # type: ignore[typeddict-item]
    if "ProductArn" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["product_arn"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ProductArn"]
            )
        )
    if "AwsAccountId" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["aws_account_id"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["AwsAccountId"]
            )
        )
    if "Id" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["id"] = aws_sdk_securityhub.types.string_filter_list.deserialize_json(
            data["Id"]
        )
    if "GeneratorId" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["generator_id"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["GeneratorId"]
            )
        )
    if "Type" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["type"] = aws_sdk_securityhub.types.string_filter_list.deserialize_json(
            data["Type"]
        )
    if "FirstObservedAt" in data:
        import aws_sdk_securityhub.types.date_filter_list

        out["first_observed_at"] = (
            aws_sdk_securityhub.types.date_filter_list.deserialize_json(
                data["FirstObservedAt"]
            )
        )
    if "LastObservedAt" in data:
        import aws_sdk_securityhub.types.date_filter_list

        out["last_observed_at"] = (
            aws_sdk_securityhub.types.date_filter_list.deserialize_json(
                data["LastObservedAt"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_securityhub.types.date_filter_list

        out["created_at"] = aws_sdk_securityhub.types.date_filter_list.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.date_filter_list

        out["updated_at"] = aws_sdk_securityhub.types.date_filter_list.deserialize_json(
            data["UpdatedAt"]
        )
    if "Confidence" in data:
        import aws_sdk_securityhub.types.number_filter_list

        out["confidence"] = (
            aws_sdk_securityhub.types.number_filter_list.deserialize_json(
                data["Confidence"]
            )
        )
    if "Criticality" in data:
        import aws_sdk_securityhub.types.number_filter_list

        out["criticality"] = (
            aws_sdk_securityhub.types.number_filter_list.deserialize_json(
                data["Criticality"]
            )
        )
    if "Title" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["title"] = aws_sdk_securityhub.types.string_filter_list.deserialize_json(
            data["Title"]
        )
    if "Description" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["description"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["Description"]
            )
        )
    if "SourceUrl" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["source_url"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["SourceUrl"]
            )
        )
    if "ProductName" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["product_name"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ProductName"]
            )
        )
    if "CompanyName" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["company_name"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["CompanyName"]
            )
        )
    if "SeverityLabel" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["severity_label"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["SeverityLabel"]
            )
        )
    if "ResourceType" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["resource_type"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceType"]
            )
        )
    if "ResourceId" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["resource_id"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceId"]
            )
        )
    if "ResourcePartition" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["resource_partition"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ResourcePartition"]
            )
        )
    if "ResourceRegion" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["resource_region"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceRegion"]
            )
        )
    if "ResourceTags" in data:
        import aws_sdk_securityhub.types.map_filter_list

        out["resource_tags"] = (
            aws_sdk_securityhub.types.map_filter_list.deserialize_json(
                data["ResourceTags"]
            )
        )
    if "ResourceDetailsOther" in data:
        import aws_sdk_securityhub.types.map_filter_list

        out["resource_details_other"] = (
            aws_sdk_securityhub.types.map_filter_list.deserialize_json(
                data["ResourceDetailsOther"]
            )
        )
    if "ComplianceStatus" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["compliance_status"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ComplianceStatus"]
            )
        )
    if "ComplianceSecurityControlId" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["compliance_security_control_id"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ComplianceSecurityControlId"]
            )
        )
    if "ComplianceAssociatedStandardsId" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["compliance_associated_standards_id"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ComplianceAssociatedStandardsId"]
            )
        )
    if "VerificationState" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["verification_state"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["VerificationState"]
            )
        )
    if "WorkflowStatus" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["workflow_status"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["WorkflowStatus"]
            )
        )
    if "RecordState" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["record_state"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["RecordState"]
            )
        )
    if "RelatedFindingsProductArn" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["related_findings_product_arn"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["RelatedFindingsProductArn"]
            )
        )
    if "RelatedFindingsId" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["related_findings_id"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["RelatedFindingsId"]
            )
        )
    if "NoteText" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["note_text"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["NoteText"]
            )
        )
    if "NoteUpdatedAt" in data:
        import aws_sdk_securityhub.types.date_filter_list

        out["note_updated_at"] = (
            aws_sdk_securityhub.types.date_filter_list.deserialize_json(
                data["NoteUpdatedAt"]
            )
        )
    if "NoteUpdatedBy" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["note_updated_by"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["NoteUpdatedBy"]
            )
        )
    if "UserDefinedFields" in data:
        import aws_sdk_securityhub.types.map_filter_list

        out["user_defined_fields"] = (
            aws_sdk_securityhub.types.map_filter_list.deserialize_json(
                data["UserDefinedFields"]
            )
        )
    if "ResourceApplicationArn" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["resource_application_arn"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceApplicationArn"]
            )
        )
    if "ResourceApplicationName" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["resource_application_name"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["ResourceApplicationName"]
            )
        )
    if "AwsAccountName" in data:
        import aws_sdk_securityhub.types.string_filter_list

        out["aws_account_name"] = (
            aws_sdk_securityhub.types.string_filter_list.deserialize_json(
                data["AwsAccountName"]
            )
        )
    return out
