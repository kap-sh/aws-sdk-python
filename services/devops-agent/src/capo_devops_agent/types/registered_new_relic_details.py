"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredNewRelicDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.new_relic_region


class RegisteredNewRelicDetails(TypedDict, closed=True):
    account_id: "str"
    """<p>The NewRelic account ID.</p>"""
    region: "capo_devops_agent.types.new_relic_region.NewRelicRegion"
    """<p>The NewRelic region (determines API endpoint).</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>Optional user description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredNewRelicDetails) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_devops_agent.types.new_relic_region

    out["region"] = capo_devops_agent.types.new_relic_region.serialize_json(
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
        import capo_devops_agent.types.new_relic_region

        out["region"] = capo_devops_agent.types.new_relic_region.deserialize_json(
            data["region"]
        )
    else:
        raise DeserializationError("RegisteredNewRelicDetails.region required")
    if "description" in data:
        out["description"] = data["description"]
    return out
