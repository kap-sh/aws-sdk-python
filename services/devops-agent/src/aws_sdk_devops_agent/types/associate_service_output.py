"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssociateServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.association
    import aws_sdk_devops_agent.types.generic_webhook


class AssociateServiceOutput(TypedDict, closed=True):
    association: "aws_sdk_devops_agent.types.association.Association"
    webhook: NotRequired["aws_sdk_devops_agent.types.generic_webhook.GenericWebhook"]
    """<p>Generic webhook configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateServiceOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.association

    out["association"] = aws_sdk_devops_agent.types.association.serialize_json(
        value["association"]
    )
    if "webhook" in value:
        import aws_sdk_devops_agent.types.generic_webhook

        out["webhook"] = aws_sdk_devops_agent.types.generic_webhook.serialize_json(
            value["webhook"]
        )
    return out


def deserialize_json(data: dict) -> AssociateServiceOutput:
    out: AssociateServiceOutput = {}  # type: ignore[typeddict-item]
    if "association" in data:
        import aws_sdk_devops_agent.types.association

        out["association"] = aws_sdk_devops_agent.types.association.deserialize_json(
            data["association"]
        )
    else:
        raise DeserializationError("AssociateServiceOutput.association required")
    if "webhook" in data:
        import aws_sdk_devops_agent.types.generic_webhook

        out["webhook"] = aws_sdk_devops_agent.types.generic_webhook.deserialize_json(
            data["webhook"]
        )
    return out
