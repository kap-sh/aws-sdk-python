"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredNewRelicDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.new_relic_region


class RegisteredNewRelicDetails(TypedDict):
    account_id: "str"
    """<p>The NewRelic account ID.</p>"""
    region: "aws_sdk_devops_agent.types.new_relic_region.NewRelicRegion"
    """<p>The NewRelic region (determines API endpoint).</p>"""
    description: NotRequired["aws_sdk_devops_agent.types.description.Description"]
    """<p>Optional user description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredNewRelicDetails) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import aws_sdk_devops_agent.types.new_relic_region

    out["region"] = aws_sdk_devops_agent.types.new_relic_region.serialize_json(
        value["region"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> RegisteredNewRelicDetails:
    out: RegisteredNewRelicDetails = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("RegisteredNewRelicDetails.account_id required")
    if "region" in data:
        import aws_sdk_devops_agent.types.new_relic_region

        out["region"] = aws_sdk_devops_agent.types.new_relic_region.deserialize_json(
            data["region"]
        )
    else:
        raise DeserializationError("RegisteredNewRelicDetails.region required")
    if "description" in data:
        out["description"] = data["description"]
    return out
