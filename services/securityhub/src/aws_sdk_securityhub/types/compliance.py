"""Generated from Smithy shape ``com.amazonaws.securityhub#Compliance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.associated_standards_list
    import aws_sdk_securityhub.types.compliance_status
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.related_requirements_list
    import aws_sdk_securityhub.types.security_control_parameters_list
    import aws_sdk_securityhub.types.status_reasons_list


class Compliance(TypedDict):
    status: NotRequired["aws_sdk_securityhub.types.compliance_status.ComplianceStatus"]
    """<p>Typically summarizes the result of a control check.</p> <p>For Security Hub CSPM controls, valid values for <code>Status</code> are as follows.</p> <ul> <li> <ul> <li> <p> <code>PASSED</code> - Standards check passed for all evaluated resources.</p> </li> <li> <p> <code>WARNING</code> - Some information is missing or this check is not supported for your configuration.</p> </li> <li> <p> <code>FAILED</code> - Standards check failed for at least one evaluated resource.</p> </li> <li> <p> <code>NOT_AVAILABLE</code> - Check could not be performed due to a service outage, API error, or because the result of the Config evaluation was <code>NOT_APPLICABLE</code>. If the Config evaluation result was <code>NOT_APPLICABLE</code> for a Security Hub CSPM control, Security Hub CSPM automatically archives the finding after 3 days.</p> </li> </ul> </li> </ul>"""
    related_requirements: NotRequired[
        "aws_sdk_securityhub.types.related_requirements_list.RelatedRequirementsList"
    ]
    """<p>Typically provides the industry or regulatory framework requirements that are related to a control. The check for that control is aligned with these requirements.</p> <p>Array Members: Maximum number of 32 items.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_securityhub.types.status_reasons_list.StatusReasonsList"
    ]
    """<p>Typically used to provide a list of reasons for the value of <code>Status</code>.</p>"""
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Typically provides the unique identifier of a control across standards. For Security Hub CSPM controls, this field consists of an Amazon Web Services service and a unique number, such as <code>APIGateway.5</code>. </p>"""
    associated_standards: NotRequired[
        "aws_sdk_securityhub.types.associated_standards_list.AssociatedStandardsList"
    ]
    """<p>Typically provides an array of enabled security standards in which a security control is currently enabled. </p>"""
    security_control_parameters: NotRequired[
        "aws_sdk_securityhub.types.security_control_parameters_list.SecurityControlParametersList"
    ]
    """<p> Typically an object that includes security control parameter names and values. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Compliance) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_securityhub.types.compliance_status

        out["Status"] = aws_sdk_securityhub.types.compliance_status.serialize_json(
            value["status"]
        )
    if "related_requirements" in value:
        import aws_sdk_securityhub.types.related_requirements_list

        out["RelatedRequirements"] = (
            aws_sdk_securityhub.types.related_requirements_list.serialize_json(
                value["related_requirements"]
            )
        )
    if "status_reasons" in value:
        import aws_sdk_securityhub.types.status_reasons_list

        out["StatusReasons"] = (
            aws_sdk_securityhub.types.status_reasons_list.serialize_json(
                value["status_reasons"]
            )
        )
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "associated_standards" in value:
        import aws_sdk_securityhub.types.associated_standards_list

        out["AssociatedStandards"] = (
            aws_sdk_securityhub.types.associated_standards_list.serialize_json(
                value["associated_standards"]
            )
        )
    if "security_control_parameters" in value:
        import aws_sdk_securityhub.types.security_control_parameters_list

        out["SecurityControlParameters"] = (
            aws_sdk_securityhub.types.security_control_parameters_list.serialize_json(
                value["security_control_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Compliance:
    out: Compliance = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_securityhub.types.compliance_status

        out["status"] = aws_sdk_securityhub.types.compliance_status.deserialize_json(
            data["Status"]
        )
    if "RelatedRequirements" in data:
        import aws_sdk_securityhub.types.related_requirements_list

        out["related_requirements"] = (
            aws_sdk_securityhub.types.related_requirements_list.deserialize_json(
                data["RelatedRequirements"]
            )
        )
    if "StatusReasons" in data:
        import aws_sdk_securityhub.types.status_reasons_list

        out["status_reasons"] = (
            aws_sdk_securityhub.types.status_reasons_list.deserialize_json(
                data["StatusReasons"]
            )
        )
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "AssociatedStandards" in data:
        import aws_sdk_securityhub.types.associated_standards_list

        out["associated_standards"] = (
            aws_sdk_securityhub.types.associated_standards_list.deserialize_json(
                data["AssociatedStandards"]
            )
        )
    if "SecurityControlParameters" in data:
        import aws_sdk_securityhub.types.security_control_parameters_list

        out["security_control_parameters"] = (
            aws_sdk_securityhub.types.security_control_parameters_list.deserialize_json(
                data["SecurityControlParameters"]
            )
        )
    return out
