"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAccountPoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_name
    import aws_sdk_datazone.types.account_source
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.resolution_strategy


class CreateAccountPoolInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the account pool is created.</p>"""
    name: "aws_sdk_datazone.types.account_pool_name.AccountPoolName"
    """<p>The name of the account pool.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the account pool.</p>"""
    resolution_strategy: "aws_sdk_datazone.types.resolution_strategy.ResolutionStrategy"
    """<p>The mechanism used to resolve the account selection from the account pool.</p>"""
    account_source: "aws_sdk_datazone.types.account_source.AccountSource"
    """<p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountPoolInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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
    return out


def deserialize_json(data: dict) -> CreateAccountPoolInput:
    out: CreateAccountPoolInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAccountPoolInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "resolutionStrategy" in data:
        import aws_sdk_datazone.types.resolution_strategy

        out["resolution_strategy"] = (
            aws_sdk_datazone.types.resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccountPoolInput.resolution_strategy required"
        )
    if "accountSource" in data:
        import aws_sdk_datazone.types.account_source

        out["account_source"] = aws_sdk_datazone.types.account_source.deserialize_json(
            data["accountSource"]
        )
    else:
        raise DeserializationError("CreateAccountPoolInput.account_source required")
    return out
