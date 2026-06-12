"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestedServiceQuotaChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.applied_level_enum
    import aws_sdk_service_quotas.types.customer_service_engagement_id
    import aws_sdk_service_quotas.types.date_time
    import aws_sdk_service_quotas.types.global_quota
    import aws_sdk_service_quotas.types.quota_arn
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.quota_context_info
    import aws_sdk_service_quotas.types.quota_name
    import aws_sdk_service_quotas.types.quota_unit
    import aws_sdk_service_quotas.types.quota_value
    import aws_sdk_service_quotas.types.request_id
    import aws_sdk_service_quotas.types.request_status
    import aws_sdk_service_quotas.types.request_type
    import aws_sdk_service_quotas.types.requester
    import aws_sdk_service_quotas.types.service_code
    import aws_sdk_service_quotas.types.service_name


class RequestedServiceQuotaChange(TypedDict):
    id: NotRequired["aws_sdk_service_quotas.types.request_id.RequestId"]
    """<p>The unique identifier.</p>"""
    request_type: NotRequired["aws_sdk_service_quotas.types.request_type.RequestType"]
    """<p>The type of quota increase request. Possible values include:</p> <ul> <li> <p> <code>AutomaticManagement</code> - The request was automatically created by Service Quotas Automatic Management when quota utilization approached the limit.</p> </li> </ul> <p>If this field is not present, the request was manually created by a user.</p>"""
    case_id: NotRequired[
        "aws_sdk_service_quotas.types.customer_service_engagement_id.CustomerServiceEngagementId"
    ]
    """<p>The case ID.</p>"""
    service_code: NotRequired["aws_sdk_service_quotas.types.service_code.ServiceCode"]
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    service_name: NotRequired["aws_sdk_service_quotas.types.service_name.ServiceName"]
    """<p>Specifies the service name.</p>"""
    quota_code: NotRequired["aws_sdk_service_quotas.types.quota_code.QuotaCode"]
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    quota_name: NotRequired["aws_sdk_service_quotas.types.quota_name.QuotaName"]
    """<p>Specifies the quota name.</p>"""
    desired_value: NotRequired["aws_sdk_service_quotas.types.quota_value.QuotaValue"]
    """<p>The new, increased value for the quota.</p>"""
    status: NotRequired["aws_sdk_service_quotas.types.request_status.RequestStatus"]
    """<p>The state of the quota increase request.</p> <ul> <li> <p> <code>PENDING</code>: The quota increase request is under review by Amazon Web Services. </p> </li> <li> <p> <code>CASE_OPENED</code>: Service Quotas opened a support case to process the quota increase request. Follow-up on the support case for more information.</p> </li> <li> <p> <code>APPROVED</code>: The quota increase request is approved. </p> </li> <li> <p> <code>DENIED</code>: The quota increase request can't be approved by Service Quotas. Contact Amazon Web Services Support for more details.</p> </li> <li> <p> <code>NOT APPROVED</code>: The quota increase request can't be approved by Service Quotas. Contact Amazon Web Services Support for more details.</p> </li> <li> <p> <code>CASE_CLOSED</code>: The support case associated with this quota increase request was closed. Check the support case correspondence for the outcome of your quota request.</p> </li> <li> <p> <code>INVALID_REQUEST</code>: Service Quotas couldn't process your resource-level quota increase request because the Amazon Resource Name (ARN) specified as part of the <code>ContextId</code> is invalid.</p> </li> </ul>"""
    created: NotRequired["aws_sdk_service_quotas.types.date_time.DateTime"]
    """<p>The date and time when the quota increase request was received and the case ID was created.</p>"""
    last_updated: NotRequired["aws_sdk_service_quotas.types.date_time.DateTime"]
    """<p>The date and time of the most recent change.</p>"""
    requester: NotRequired["aws_sdk_service_quotas.types.requester.Requester"]
    """<p>The IAM identity of the requester.</p>"""
    quota_arn: NotRequired["aws_sdk_service_quotas.types.quota_arn.QuotaArn"]
    """<p>The Amazon Resource Name (ARN) of the quota.</p>"""
    global_quota: "aws_sdk_service_quotas.types.global_quota.GlobalQuota"
    """<p>Indicates whether the quota is global.</p>"""
    unit: NotRequired["aws_sdk_service_quotas.types.quota_unit.QuotaUnit"]
    """<p>The unit of measurement.</p>"""
    quota_requested_at_level: NotRequired[
        "aws_sdk_service_quotas.types.applied_level_enum.AppliedLevelEnum"
    ]
    """<p>Filters the response to return quota requests for the <code>ACCOUNT</code>, <code>RESOURCE</code>, or <code>ALL</code> levels. <code>ACCOUNT</code> is the default.</p>"""
    quota_context: NotRequired[
        "aws_sdk_service_quotas.types.quota_context_info.QuotaContextInfo"
    ]
    """<p>The context for this service quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestedServiceQuotaChange) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "request_type" in value:
        import aws_sdk_service_quotas.types.request_type

        out["RequestType"] = (
            aws_sdk_service_quotas.types.request_type.serialize_aws_json_1_1(
                value["request_type"]
            )
        )
    if "case_id" in value:
        out["CaseId"] = value["case_id"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "quota_name" in value:
        out["QuotaName"] = value["quota_name"]
    if "desired_value" in value:
        out["DesiredValue"] = value["desired_value"]
    if "status" in value:
        import aws_sdk_service_quotas.types.request_status

        out["Status"] = (
            aws_sdk_service_quotas.types.request_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created" in value:
        import aws_sdk_service_quotas.types.date_time

        out["Created"] = aws_sdk_service_quotas.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_updated" in value:
        import aws_sdk_service_quotas.types.date_time

        out["LastUpdated"] = (
            aws_sdk_service_quotas.types.date_time.serialize_aws_json_1_1(
                value["last_updated"]
            )
        )
    if "requester" in value:
        out["Requester"] = value["requester"]
    if "quota_arn" in value:
        out["QuotaArn"] = value["quota_arn"]
    out["GlobalQuota"] = value.get("global_quota", False)
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "quota_requested_at_level" in value:
        import aws_sdk_service_quotas.types.applied_level_enum

        out["QuotaRequestedAtLevel"] = (
            aws_sdk_service_quotas.types.applied_level_enum.serialize_aws_json_1_1(
                value["quota_requested_at_level"]
            )
        )
    if "quota_context" in value:
        import aws_sdk_service_quotas.types.quota_context_info

        out["QuotaContext"] = (
            aws_sdk_service_quotas.types.quota_context_info.serialize_aws_json_1_1(
                value["quota_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestedServiceQuotaChange:
    out: RequestedServiceQuotaChange = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "RequestType" in data:
        import aws_sdk_service_quotas.types.request_type

        out["request_type"] = (
            aws_sdk_service_quotas.types.request_type.deserialize_aws_json_1_1(
                data["RequestType"]
            )
        )
    if "CaseId" in data:
        out["case_id"] = data["CaseId"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "QuotaName" in data:
        out["quota_name"] = data["QuotaName"]
    if "DesiredValue" in data:
        out["desired_value"] = data["DesiredValue"]
    if "Status" in data:
        import aws_sdk_service_quotas.types.request_status

        out["status"] = (
            aws_sdk_service_quotas.types.request_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Created" in data:
        import aws_sdk_service_quotas.types.date_time

        out["created"] = (
            aws_sdk_service_quotas.types.date_time.deserialize_aws_json_1_1(
                data["Created"]
            )
        )
    if "LastUpdated" in data:
        import aws_sdk_service_quotas.types.date_time

        out["last_updated"] = (
            aws_sdk_service_quotas.types.date_time.deserialize_aws_json_1_1(
                data["LastUpdated"]
            )
        )
    if "Requester" in data:
        out["requester"] = data["Requester"]
    if "QuotaArn" in data:
        out["quota_arn"] = data["QuotaArn"]
    if "GlobalQuota" in data:
        out["global_quota"] = data["GlobalQuota"]
    else:
        out["global_quota"] = False
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "QuotaRequestedAtLevel" in data:
        import aws_sdk_service_quotas.types.applied_level_enum

        out["quota_requested_at_level"] = (
            aws_sdk_service_quotas.types.applied_level_enum.deserialize_aws_json_1_1(
                data["QuotaRequestedAtLevel"]
            )
        )
    if "QuotaContext" in data:
        import aws_sdk_service_quotas.types.quota_context_info

        out["quota_context"] = (
            aws_sdk_service_quotas.types.quota_context_info.deserialize_aws_json_1_1(
                data["QuotaContext"]
            )
        )
    return out
