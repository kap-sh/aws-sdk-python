"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateAccountPoolOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.account_pool_id
    import aws_sdk_datazone.types.account_pool_name
    import aws_sdk_datazone.types.account_source
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.resolution_strategy
    import aws_sdk_datazone.types.updated_by


class UpdateAccountPoolOutput(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The domain ID where the account pool that is to be updated lives.</p>"""
    name: NotRequired["aws_sdk_datazone.types.account_pool_name.AccountPoolName"]
    """<p>The name of the account pool that is to be updated.</p>"""
    id: NotRequired["aws_sdk_datazone.types.account_pool_id.AccountPoolId"]
    """<p>The ID of the account pool that is to be updated.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the account pool that is to be udpated.</p>"""
    resolution_strategy: NotRequired[
        "aws_sdk_datazone.types.resolution_strategy.ResolutionStrategy"
    ]
    """<p>The mechanism used to resolve the account selection from the account pool.</p>"""
    account_source: "aws_sdk_datazone.types.account_source.AccountSource"
    """<p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The user who created the account pool.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the account pool was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the account pool was last updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who last updated the account pool.</p>"""
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The domain ID in which the account pool that is to be updated lives.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountPoolOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "resolution_strategy" in value:
        import aws_sdk_datazone.types.resolution_strategy

        out["resolutionStrategy"] = (
            aws_sdk_datazone.types.resolution_strategy.serialize_json(
                value["resolution_strategy"]
            )
        )
    import aws_sdk_datazone.types.account_source

    out["accountSource"] = aws_sdk_datazone.types.account_source.serialize_json(
        value["account_source"]
    )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lastUpdatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    return out


def deserialize_json(data: dict) -> UpdateAccountPoolOutput:
    out: UpdateAccountPoolOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "resolutionStrategy" in data:
        import aws_sdk_datazone.types.resolution_strategy

        out["resolution_strategy"] = (
            aws_sdk_datazone.types.resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    if "accountSource" in data:
        import aws_sdk_datazone.types.account_source

        out["account_source"] = aws_sdk_datazone.types.account_source.deserialize_json(
            data["accountSource"]
        )
    else:
        raise DeserializationError("UpdateAccountPoolOutput.account_source required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("UpdateAccountPoolOutput.created_by required")
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    return out
