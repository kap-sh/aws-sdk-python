"""Generated from Smithy shape ``com.amazonaws.glue#ResourceUri``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.resource_type
    import capo_glue.types.uri


class ResourceUri(TypedDict, closed=True):
    resource_type: NotRequired["capo_glue.types.resource_type.ResourceType"]
    """<p>The type of the resource.</p>"""
    uri: NotRequired["capo_glue.types.uri.URI"]
    """<p>The URI for accessing the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUri) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_glue.types.resource_type

        out["ResourceType"] = capo_glue.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "uri" in value:
        out["Uri"] = value["uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUri:
    out: ResourceUri = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_glue.types.resource_type

        out["resource_type"] = capo_glue.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    if "Uri" in data:
        out["uri"] = data["Uri"]
    return out
