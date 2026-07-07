"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.entitlement_usage_list


class LicenseUsage(TypedDict, closed=True):
    entitlement_usages: NotRequired[
        "aws_sdk_license_manager.types.entitlement_usage_list.EntitlementUsageList"
    ]
    """<p>License entitlement usages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseUsage) -> dict:
    out: dict = {}
    if "entitlement_usages" in value:
        import aws_sdk_license_manager.types.entitlement_usage_list

        out["EntitlementUsages"] = (
            aws_sdk_license_manager.types.entitlement_usage_list.serialize_aws_json_1_1(
                value["entitlement_usages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseUsage:
    out: LicenseUsage = {}  # type: ignore[typeddict-item]
    if "EntitlementUsages" in data:
        import aws_sdk_license_manager.types.entitlement_usage_list

        out["entitlement_usages"] = (
            aws_sdk_license_manager.types.entitlement_usage_list.deserialize_aws_json_1_1(
                data["EntitlementUsages"]
            )
        )
    return out
