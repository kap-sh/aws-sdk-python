"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StartCompositionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition_client_token
    import aws_sdk_ivs_realtime.types.destination_configuration_list
    import aws_sdk_ivs_realtime.types.layout_configuration
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.tags


class StartCompositionRequest(TypedDict):
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to be used for compositing.</p>"""
    idempotency_token: NotRequired[
        "aws_sdk_ivs_realtime.types.composition_client_token.CompositionClientToken"
    ]
    """<p>Idempotency token.</p>"""
    layout: NotRequired[
        "aws_sdk_ivs_realtime.types.layout_configuration.LayoutConfiguration"
    ]
    """<p>Layout object to configure composition parameters.</p>"""
    destinations: "aws_sdk_ivs_realtime.types.destination_configuration_list.DestinationConfigurationList"
    """<p>Array of destination configuration.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCompositionRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    if "layout" in value:
        import aws_sdk_ivs_realtime.types.layout_configuration

        out["layout"] = aws_sdk_ivs_realtime.types.layout_configuration.serialize_json(
            value["layout"]
        )
    import aws_sdk_ivs_realtime.types.destination_configuration_list

    out["destinations"] = (
        aws_sdk_ivs_realtime.types.destination_configuration_list.serialize_json(
            value["destinations"]
        )
    )
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartCompositionRequest:
    out: StartCompositionRequest = {}  # type: ignore[typeddict-item]
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("StartCompositionRequest.stage_arn required")
    if "idempotencyToken" in data:
        out["idempotency_token"] = data["idempotencyToken"]
    if "layout" in data:
        import aws_sdk_ivs_realtime.types.layout_configuration

        out["layout"] = (
            aws_sdk_ivs_realtime.types.layout_configuration.deserialize_json(
                data["layout"]
            )
        )
    if "destinations" in data:
        import aws_sdk_ivs_realtime.types.destination_configuration_list

        out["destinations"] = (
            aws_sdk_ivs_realtime.types.destination_configuration_list.deserialize_json(
                data["destinations"]
            )
        )
    else:
        raise DeserializationError("StartCompositionRequest.destinations required")
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
