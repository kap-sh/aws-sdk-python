"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.association
    import capo_devops_agent.types.generic_webhook


class UpdateAssociationOutput(TypedDict, closed=True):
    association: "capo_devops_agent.types.association.Association"
    webhook: NotRequired["capo_devops_agent.types.generic_webhook.GenericWebhook"]
    """<p>Generic webhook configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssociationOutput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.association

    out["association"] = capo_devops_agent.types.association.serialize_json(
        value["association"]
    )
    if "webhook" in value:
        import capo_devops_agent.types.generic_webhook

        out["webhook"] = capo_devops_agent.types.generic_webhook.serialize_json(
            value["webhook"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssociationOutput:
    out: UpdateAssociationOutput = {}  # type: ignore[typeddict-item]
    if "association" in data:
        import capo_devops_agent.types.association

        out["association"] = capo_devops_agent.types.association.deserialize_json(
            data["association"]
        )
    else:
        raise DeserializationError("UpdateAssociationOutput.association required")
    if "webhook" in data:
        import capo_devops_agent.types.generic_webhook

        out["webhook"] = capo_devops_agent.types.generic_webhook.deserialize_json(
            data["webhook"]
        )
    return out
