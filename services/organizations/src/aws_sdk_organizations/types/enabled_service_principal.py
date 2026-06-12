"""Generated from Smithy shape ``com.amazonaws.organizations#EnabledServicePrincipal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.service_principal
    import aws_sdk_organizations.types.timestamp


class EnabledServicePrincipal(TypedDict):
    service_principal: NotRequired[
        "aws_sdk_organizations.types.service_principal.ServicePrincipal"
    ]
    """<p>The name of the service principal. This is typically in the form of a URL, such as: <code> <i>servicename</i>.amazonaws.com</code>.</p>"""
    date_enabled: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>The date that the service principal was enabled for integration with Organizations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnabledServicePrincipal) -> dict:
    out: dict = {}
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "date_enabled" in value:
        import aws_sdk_organizations.types.timestamp

        out["DateEnabled"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["date_enabled"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnabledServicePrincipal:
    out: EnabledServicePrincipal = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    if "DateEnabled" in data:
        import aws_sdk_organizations.types.timestamp

        out["date_enabled"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["DateEnabled"]
            )
        )
    return out
