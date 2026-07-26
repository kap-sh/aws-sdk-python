"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateHostOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.host_arn
    import capo_codestar_connections.types.tag_list


class CreateHostOutput(TypedDict, closed=True):
    host_arn: NotRequired["capo_codestar_connections.types.host_arn.HostArn"]
    """<p>The Amazon Resource Name (ARN) of the host to be created.</p>"""
    tags: NotRequired["capo_codestar_connections.types.tag_list.TagList"]
    """<p>Tags for the created host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateHostOutput) -> dict:
    out: dict = {}
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    if "tags" in value:
        import capo_codestar_connections.types.tag_list

        out["Tags"] = capo_codestar_connections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateHostOutput:
    out: CreateHostOutput = {}  # type: ignore[typeddict-item]
    if "HostArn" in data:
        out["host_arn"] = data["HostArn"]
    if "Tags" in data:
        import capo_codestar_connections.types.tag_list

        out["tags"] = capo_codestar_connections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
