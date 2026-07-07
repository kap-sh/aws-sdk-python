"""Generated from Smithy shape ``com.amazonaws.schemas#CreateDiscovererRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__boolean
    import aws_sdk_schemas.types.__string_min0_max256
    import aws_sdk_schemas.types.__string_min20_max1600
    import aws_sdk_schemas.types.tags


class CreateDiscovererRequest(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>A description for the discoverer.</p>"""
    source_arn: NotRequired[
        "aws_sdk_schemas.types.__string_min20_max1600.__stringMin20Max1600"
    ]
    """<p>The ARN of the event bus.</p>"""
    cross_account: NotRequired["aws_sdk_schemas.types.__boolean.__boolean"]
    """<p>Support discovery of schemas in events sent to the bus from another account. (default: true).</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    """<p>Tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDiscovererRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "cross_account" in value:
        out["CrossAccount"] = value["cross_account"]
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDiscovererRequest:
    out: CreateDiscovererRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "CrossAccount" in data:
        out["cross_account"] = data["CrossAccount"]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    return out
