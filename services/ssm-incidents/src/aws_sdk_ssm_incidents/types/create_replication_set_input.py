"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateReplicationSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.region_map_input
    import aws_sdk_ssm_incidents.types.tag_map


class CreateReplicationSetInput(TypedDict, closed=True):
    regions: "aws_sdk_ssm_incidents.types.region_map_input.RegionMapInput"
    """<p>The Regions that Incident Manager replicates your data to. You can have up to three Regions in your replication set.</p>"""
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""
    tags: NotRequired["aws_sdk_ssm_incidents.types.tag_map.TagMap"]
    """<p>A list of tags to add to the replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicationSetInput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.region_map_input

    out["regions"] = aws_sdk_ssm_incidents.types.region_map_input.serialize_json(
        value["regions"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_ssm_incidents.types.tag_map

        out["tags"] = aws_sdk_ssm_incidents.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateReplicationSetInput:
    out: CreateReplicationSetInput = {}  # type: ignore[typeddict-item]
    if "regions" in data:
        import aws_sdk_ssm_incidents.types.region_map_input

        out["regions"] = aws_sdk_ssm_incidents.types.region_map_input.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("CreateReplicationSetInput.regions required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_ssm_incidents.types.tag_map

        out["tags"] = aws_sdk_ssm_incidents.types.tag_map.deserialize_json(data["tags"])
    return out
