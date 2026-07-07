"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateApplicationFromEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.string


class DisassociateApplicationFromEntitlementRequest(TypedDict, closed=True):
    stack_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the stack with which the entitlement is associated.</p>"""
    entitlement_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    application_identifier: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The identifier of the application to remove from the entitlement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateApplicationFromEntitlementRequest,
) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "entitlement_name" in value:
        out["EntitlementName"] = value["entitlement_name"]
    if "application_identifier" in value:
        out["ApplicationIdentifier"] = value["application_identifier"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateApplicationFromEntitlementRequest:
    out: DisassociateApplicationFromEntitlementRequest = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "EntitlementName" in data:
        out["entitlement_name"] = data["EntitlementName"]
    if "ApplicationIdentifier" in data:
        out["application_identifier"] = data["ApplicationIdentifier"]
    return out
