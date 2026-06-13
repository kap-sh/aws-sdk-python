"""Generated from Smithy shape ``com.amazonaws.datazone#PostLineageEventInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.lineage_event


class PostLineageEventInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to post a data lineage event.</p>"""
    event: "aws_sdk_datazone.types.lineage_event.LineageEvent"
    """<p>The data lineage event that you want to post. Only open-lineage run event are supported as events. </p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostLineageEventInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.lineage_event

    out["event"] = aws_sdk_datazone.types.lineage_event.serialize_json(value["event"])
    return out


def deserialize_json(data: dict) -> PostLineageEventInput:
    out: PostLineageEventInput = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import aws_sdk_datazone.types.lineage_event

        out["event"] = aws_sdk_datazone.types.lineage_event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("PostLineageEventInput.event required")
    return out
