"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PublicKeySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.public_key_arn
    import aws_sdk_ivs_realtime.types.public_key_name
    import aws_sdk_ivs_realtime.types.tags


class PublicKeySummary(TypedDict):
    arn: NotRequired["aws_sdk_ivs_realtime.types.public_key_arn.PublicKeyArn"]
    """<p>Public key ARN.</p>"""
    name: NotRequired["aws_sdk_ivs_realtime.types.public_key_name.PublicKeyName"]
    """<p>Public key name.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicKeySummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PublicKeySummary:
    out: PublicKeySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
