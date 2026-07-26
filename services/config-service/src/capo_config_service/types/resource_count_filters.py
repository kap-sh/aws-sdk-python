"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCountFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.resource_type


class ResourceCountFilters(TypedDict, closed=True):
    resource_type: NotRequired["capo_config_service.types.resource_type.ResourceType"]
    """<p>The type of the Amazon Web Services resource.</p>"""
    account_id: NotRequired["capo_config_service.types.account_id.AccountId"]
    """<p>The 12-digit ID of the account.</p>"""
    region: NotRequired["capo_config_service.types.aws_region.AwsRegion"]
    """<p>The region where the account is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCountFilters) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_config_service.types.resource_type

        out["ResourceType"] = (
            capo_config_service.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceCountFilters:
    out: ResourceCountFilters = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
