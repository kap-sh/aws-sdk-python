"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetIndexOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resource_explorer_2.types.index_state
    import aws_sdk_resource_explorer_2.types.index_type
    import aws_sdk_resource_explorer_2.types.region_list
    import aws_sdk_resource_explorer_2.types.tag_map


class GetIndexOutput(TypedDict):
    arn: NotRequired["str"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the index.</p>"""
    type: NotRequired["aws_sdk_resource_explorer_2.types.index_type.IndexType"]
    r"""<p>The type of the index in this Region. For information about the aggregator index and how it differs from a local index, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html\">Turning on cross-Region search by creating an aggregator index</a>.</p>"""
    state: NotRequired["aws_sdk_resource_explorer_2.types.index_state.IndexState"]
    """<p>The current state of the index in this Amazon Web Services Region.</p>"""
    replicating_from: NotRequired[
        "aws_sdk_resource_explorer_2.types.region_list.RegionList"
    ]
    """<p>This response value is present only if this index is <code>Type=AGGREGATOR</code>.</p> <p>A list of the Amazon Web Services Regions that replicate their content to the index in this Region.</p>"""
    replicating_to: NotRequired[
        "aws_sdk_resource_explorer_2.types.region_list.RegionList"
    ]
    """<p>This response value is present only if this index is <code>Type=LOCAL</code>.</p> <p>The Amazon Web Services Region that contains the aggregator index, if one exists. If an aggregator index does exist then the Region in which you called this operation replicates its index information to the Region specified in this response value. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the index was originally created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the index was last updated.</p>"""
    tags: NotRequired["aws_sdk_resource_explorer_2.types.tag_map.TagMap"]
    """<p>Tag key and value pairs that are attached to the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "state" in value:
        out["State"] = value["state"]
    if "replicating_from" in value:
        import aws_sdk_resource_explorer_2.types.region_list

        out["ReplicatingFrom"] = (
            aws_sdk_resource_explorer_2.types.region_list.serialize_json(
                value["replicating_from"]
            )
        )
    if "replicating_to" in value:
        import aws_sdk_resource_explorer_2.types.region_list

        out["ReplicatingTo"] = (
            aws_sdk_resource_explorer_2.types.region_list.serialize_json(
                value["replicating_to"]
            )
        )
    if "created_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "tags" in value:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["Tags"] = aws_sdk_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetIndexOutput:
    out: GetIndexOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "State" in data:
        out["state"] = data["State"]
    if "ReplicatingFrom" in data:
        import aws_sdk_resource_explorer_2.types.region_list

        out["replicating_from"] = (
            aws_sdk_resource_explorer_2.types.region_list.deserialize_json(
                data["ReplicatingFrom"]
            )
        )
    if "ReplicatingTo" in data:
        import aws_sdk_resource_explorer_2.types.region_list

        out["replicating_to"] = (
            aws_sdk_resource_explorer_2.types.region_list.deserialize_json(
                data["ReplicatingTo"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Tags" in data:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["tags"] = aws_sdk_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
