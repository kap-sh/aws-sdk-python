"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListWebhooksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.webhooks_list


class ListWebhooksOutput(TypedDict):
    webhooks: "aws_sdk_devops_agent.types.webhooks_list.WebhooksList"
    """<p>The list of association webhooks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebhooksOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.webhooks_list

    out["webhooks"] = aws_sdk_devops_agent.types.webhooks_list.serialize_json(
        value["webhooks"]
    )
    return out


def deserialize_json(data: dict) -> ListWebhooksOutput:
    out: ListWebhooksOutput = {}  # type: ignore[typeddict-item]
    if "webhooks" in data:
        import aws_sdk_devops_agent.types.webhooks_list

        out["webhooks"] = aws_sdk_devops_agent.types.webhooks_list.deserialize_json(
            data["webhooks"]
        )
    else:
        raise DeserializationError("ListWebhooksOutput.webhooks required")
    return out
