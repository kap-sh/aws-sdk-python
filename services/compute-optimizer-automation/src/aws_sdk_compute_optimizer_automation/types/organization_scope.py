"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids


class OrganizationScope(TypedDict):
    account_ids: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids.OrganizationConfigurationAccountIds"
    ]
    """<p>List of Amazon Web Services account IDs to include in the organization scope.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrganizationScope) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OrganizationScope:
    out: OrganizationScope = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids

        out["account_ids"] = (
            aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    return out
