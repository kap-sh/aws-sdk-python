"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#EncoderConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.encoder_configuration_arn
    import aws_sdk_ivs_realtime.types.encoder_configuration_name
    import aws_sdk_ivs_realtime.types.tags


class EncoderConfigurationSummary(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    """<p>ARN of the EncoderConfiguration resource.</p>"""
    name: NotRequired[
        "aws_sdk_ivs_realtime.types.encoder_configuration_name.EncoderConfigurationName"
    ]
    """<p>Optional name to identify the resource.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncoderConfigurationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EncoderConfigurationSummary:
    out: EncoderConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EncoderConfigurationSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
