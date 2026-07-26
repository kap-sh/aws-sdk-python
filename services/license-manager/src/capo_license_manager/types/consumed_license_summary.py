"""Generated from Smithy shape ``com.amazonaws.licensemanager#ConsumedLicenseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.box_long
    import capo_license_manager.types.resource_type


class ConsumedLicenseSummary(TypedDict, closed=True):
    resource_type: NotRequired["capo_license_manager.types.resource_type.ResourceType"]
    """<p>Resource type of the resource consuming a license.</p>"""
    consumed_licenses: NotRequired["capo_license_manager.types.box_long.BoxLong"]
    """<p>Number of licenses consumed by the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumedLicenseSummary) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_license_manager.types.resource_type

        out["ResourceType"] = (
            capo_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "consumed_licenses" in value:
        out["ConsumedLicenses"] = value["consumed_licenses"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConsumedLicenseSummary:
    out: ConsumedLicenseSummary = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_license_manager.types.resource_type

        out["resource_type"] = (
            capo_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ConsumedLicenses" in data:
        out["consumed_licenses"] = data["ConsumedLicenses"]
    return out
