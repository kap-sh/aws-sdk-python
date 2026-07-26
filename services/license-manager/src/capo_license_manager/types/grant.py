"""Generated from Smithy shape ``com.amazonaws.licensemanager#Grant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.arn
    import capo_license_manager.types.grant_status
    import capo_license_manager.types.options
    import capo_license_manager.types.status_reason_message
    import capo_license_manager.types.string


class Grant(TypedDict, closed=True):
    grant_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""
    grant_name: "capo_license_manager.types.string.String"
    """<p>Grant name.</p>"""
    parent_arn: "capo_license_manager.types.arn.Arn"
    """<p>Parent ARN.</p>"""
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>License ARN.</p>"""
    grantee_principal_arn: "capo_license_manager.types.arn.Arn"
    """<p>The grantee principal ARN.</p>"""
    home_region: "capo_license_manager.types.string.String"
    """<p>Home Region of the grant.</p>"""
    grant_status: "capo_license_manager.types.grant_status.GrantStatus"
    """<p>Grant status.</p>"""
    status_reason: NotRequired[
        "capo_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>Grant status reason.</p>"""
    version: "capo_license_manager.types.string.String"
    """<p>Grant version.</p>"""
    granted_operations: (
        "capo_license_manager.types.allowed_operation_list.AllowedOperationList"
    )
    """<p>Granted operations.</p>"""
    options: NotRequired["capo_license_manager.types.options.Options"]
    """<p>The options specified for the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Grant) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    out["GrantName"] = value["grant_name"]
    out["ParentArn"] = value["parent_arn"]
    out["LicenseArn"] = value["license_arn"]
    out["GranteePrincipalArn"] = value["grantee_principal_arn"]
    out["HomeRegion"] = value["home_region"]
    import capo_license_manager.types.grant_status

    out["GrantStatus"] = capo_license_manager.types.grant_status.serialize_aws_json_1_1(
        value["grant_status"]
    )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    out["Version"] = value["version"]
    import capo_license_manager.types.allowed_operation_list

    out["GrantedOperations"] = (
        capo_license_manager.types.allowed_operation_list.serialize_aws_json_1_1(
            value["granted_operations"]
        )
    )
    if "options" in value:
        import capo_license_manager.types.options

        out["Options"] = capo_license_manager.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Grant:
    out: Grant = {}  # type: ignore[typeddict-item]
    if "GrantArn" in data:
        out["grant_arn"] = data["GrantArn"]
    else:
        raise DeserializationError("Grant.grant_arn required")
    if "GrantName" in data:
        out["grant_name"] = data["GrantName"]
    else:
        raise DeserializationError("Grant.grant_name required")
    if "ParentArn" in data:
        out["parent_arn"] = data["ParentArn"]
    else:
        raise DeserializationError("Grant.parent_arn required")
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("Grant.license_arn required")
    if "GranteePrincipalArn" in data:
        out["grantee_principal_arn"] = data["GranteePrincipalArn"]
    else:
        raise DeserializationError("Grant.grantee_principal_arn required")
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    else:
        raise DeserializationError("Grant.home_region required")
    if "GrantStatus" in data:
        import capo_license_manager.types.grant_status

        out["grant_status"] = (
            capo_license_manager.types.grant_status.deserialize_aws_json_1_1(
                data["GrantStatus"]
            )
        )
    else:
        raise DeserializationError("Grant.grant_status required")
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("Grant.version required")
    if "GrantedOperations" in data:
        import capo_license_manager.types.allowed_operation_list

        out["granted_operations"] = (
            capo_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["GrantedOperations"]
            )
        )
    else:
        raise DeserializationError("Grant.granted_operations required")
    if "Options" in data:
        import capo_license_manager.types.options

        out["options"] = capo_license_manager.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    return out
