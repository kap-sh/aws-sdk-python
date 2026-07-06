"""Generated from Smithy shape ``com.amazonaws.datazone#AccountPoolSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_id
    import aws_sdk_datazone.types.account_pool_name
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.resolution_strategy
    import aws_sdk_datazone.types.updated_by


class AccountPoolSummary(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain.</p>"""
    id: NotRequired["aws_sdk_datazone.types.account_pool_id.AccountPoolId"]
    """<p>The ID of the account pool.</p>"""
    name: NotRequired["aws_sdk_datazone.types.account_pool_name.AccountPoolName"]
    """<p>The name of the account pool.</p>"""
    resolution_strategy: NotRequired[
        "aws_sdk_datazone.types.resolution_strategy.ResolutionStrategy"
    ]
    """<p>The mechanism used to resolve the account selection from the account pool.</p>"""
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the account pool.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the account pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountPoolSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "resolution_strategy" in value:
        import aws_sdk_datazone.types.resolution_strategy

        out["resolutionStrategy"] = (
            aws_sdk_datazone.types.resolution_strategy.serialize_json(
                value["resolution_strategy"]
            )
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> AccountPoolSummary:
    out: AccountPoolSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "resolutionStrategy" in data:
        import aws_sdk_datazone.types.resolution_strategy

        out["resolution_strategy"] = (
            aws_sdk_datazone.types.resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
