"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.registered_service
    import aws_sdk_devops_agent.types.tags


class GetServiceOutput(TypedDict, closed=True):
    service: "aws_sdk_devops_agent.types.registered_service.RegisteredService"
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags associated with the Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.registered_service

    out["service"] = aws_sdk_devops_agent.types.registered_service.serialize_json(
        value["service"]
    )
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetServiceOutput:
    out: GetServiceOutput = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_devops_agent.types.registered_service

        out["service"] = aws_sdk_devops_agent.types.registered_service.deserialize_json(
            data["service"]
        )
    else:
        raise DeserializationError("GetServiceOutput.service required")
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
