"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_id
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.framework_description
    import aws_sdk_auditmanager.types.framework_name
    import aws_sdk_auditmanager.types.nullable_integer
    import aws_sdk_auditmanager.types.region
    import aws_sdk_auditmanager.types.share_request_comment
    import aws_sdk_auditmanager.types.share_request_status
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class AssessmentFrameworkShareRequest(TypedDict):
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the share request. </p>"""
    framework_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p>The unique identifier for the shared custom framework. </p>"""
    framework_name: NotRequired[
        "aws_sdk_auditmanager.types.framework_name.FrameworkName"
    ]
    """<p> The name of the custom framework that the share request is for. </p>"""
    framework_description: NotRequired[
        "aws_sdk_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p>The description of the shared custom framework.</p>"""
    status: NotRequired[
        "aws_sdk_auditmanager.types.share_request_status.ShareRequestStatus"
    ]
    """<p> The status of the share request. </p>"""
    source_account: NotRequired["aws_sdk_auditmanager.types.account_id.AccountId"]
    """<p> The Amazon Web Services account of the sender. </p>"""
    destination_account: NotRequired["aws_sdk_auditmanager.types.account_id.AccountId"]
    """<p> The Amazon Web Services account of the recipient. </p>"""
    destination_region: NotRequired["aws_sdk_auditmanager.types.region.Region"]
    """<p> The Amazon Web Services Region of the recipient. </p>"""
    expiration_time: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the share request expires. </p>"""
    creation_time: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the share request was created. </p>"""
    last_updated: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the share request was last updated. </p>"""
    comment: NotRequired[
        "aws_sdk_auditmanager.types.share_request_comment.ShareRequestComment"
    ]
    """<p> An optional comment from the sender about the share request. </p>"""
    standard_controls_count: NotRequired[
        "aws_sdk_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of standard controls that are part of the shared custom framework. </p>"""
    custom_controls_count: NotRequired[
        "aws_sdk_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of custom controls that are part of the shared custom framework.</p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p>The compliance type that the shared custom framework supports, such as CIS or HIPAA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "framework_id" in value:
        out["frameworkId"] = value["framework_id"]
    if "framework_name" in value:
        out["frameworkName"] = value["framework_name"]
    if "framework_description" in value:
        out["frameworkDescription"] = value["framework_description"]
    if "status" in value:
        import aws_sdk_auditmanager.types.share_request_status

        out["status"] = aws_sdk_auditmanager.types.share_request_status.serialize_json(
            value["status"]
        )
    if "source_account" in value:
        out["sourceAccount"] = value["source_account"]
    if "destination_account" in value:
        out["destinationAccount"] = value["destination_account"]
    if "destination_region" in value:
        out["destinationRegion"] = value["destination_region"]
    if "expiration_time" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["expirationTime"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["expiration_time"]
        )
    if "creation_time" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["creationTime"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["lastUpdated"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "standard_controls_count" in value:
        out["standardControlsCount"] = value["standard_controls_count"]
    if "custom_controls_count" in value:
        out["customControlsCount"] = value["custom_controls_count"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    return out


def deserialize_json(data: dict) -> AssessmentFrameworkShareRequest:
    out: AssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "frameworkId" in data:
        out["framework_id"] = data["frameworkId"]
    if "frameworkName" in data:
        out["framework_name"] = data["frameworkName"]
    if "frameworkDescription" in data:
        out["framework_description"] = data["frameworkDescription"]
    if "status" in data:
        import aws_sdk_auditmanager.types.share_request_status

        out["status"] = (
            aws_sdk_auditmanager.types.share_request_status.deserialize_json(
                data["status"]
            )
        )
    if "sourceAccount" in data:
        out["source_account"] = data["sourceAccount"]
    if "destinationAccount" in data:
        out["destination_account"] = data["destinationAccount"]
    if "destinationRegion" in data:
        out["destination_region"] = data["destinationRegion"]
    if "expirationTime" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["expiration_time"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["expirationTime"]
        )
    if "creationTime" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["creation_time"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdated" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["last_updated"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    if "standardControlsCount" in data:
        out["standard_controls_count"] = data["standardControlsCount"]
    if "customControlsCount" in data:
        out["custom_controls_count"] = data["customControlsCount"]
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    return out
