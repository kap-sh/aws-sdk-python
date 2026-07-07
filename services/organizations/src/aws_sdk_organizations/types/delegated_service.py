"""Generated from Smithy shape ``com.amazonaws.organizations#DelegatedService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.service_principal
    import aws_sdk_organizations.types.timestamp


class DelegatedService(TypedDict, closed=True):
    service_principal: NotRequired[
        "aws_sdk_organizations.types.service_principal.ServicePrincipal"
    ]
    """<p>The name of an Amazon Web Services service that can request an operation for the specified service. This is typically in the form of a URL, such as: <code> <i>servicename</i>.amazonaws.com</code>.</p>"""
    delegation_enabled_date: NotRequired[
        "aws_sdk_organizations.types.timestamp.Timestamp"
    ]
    """<p>The date that the account became a delegated administrator for this service. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DelegatedService) -> dict:
    out: dict = {}
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "delegation_enabled_date" in value:
        import aws_sdk_organizations.types.timestamp

        out["DelegationEnabledDate"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["delegation_enabled_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DelegatedService:
    out: DelegatedService = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    if "DelegationEnabledDate" in data:
        import aws_sdk_organizations.types.timestamp

        out["delegation_enabled_date"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["DelegationEnabledDate"]
            )
        )
    return out
