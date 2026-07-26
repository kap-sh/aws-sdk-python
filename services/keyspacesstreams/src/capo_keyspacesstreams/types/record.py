"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.date
    import capo_keyspacesstreams.types.keyspaces_keys_map
    import capo_keyspacesstreams.types.keyspaces_row
    import capo_keyspacesstreams.types.origin_type
    import capo_keyspacesstreams.types.sequence_number


class Record(TypedDict, closed=True):
    event_version: NotRequired["str"]
    """<p>The version of the record format, used to track the evolution of the record structure over time.</p>"""
    created_at: NotRequired["capo_keyspacesstreams.types.date.Date"]
    """<p>The timestamp indicating when this change data capture record was created.</p>"""
    origin: NotRequired["capo_keyspacesstreams.types.origin_type.OriginType"]
    """<p>The origin or source of this change data capture record.</p>"""
    partition_keys: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_keys_map.KeyspacesKeysMap"
    ]
    """<p>The partition key columns and their values for the affected row.</p>"""
    clustering_keys: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_keys_map.KeyspacesKeysMap"
    ]
    """<p>The clustering key columns and their values for the affected row, which determine the order of rows within a partition.</p>"""
    new_image: NotRequired["capo_keyspacesstreams.types.keyspaces_row.KeyspacesRow"]
    """<p>The state of the row after the change operation that generated this record.</p>"""
    old_image: NotRequired["capo_keyspacesstreams.types.keyspaces_row.KeyspacesRow"]
    """<p>The state of the row before the change operation that generated this record.</p>"""
    sequence_number: NotRequired[
        "capo_keyspacesstreams.types.sequence_number.SequenceNumber"
    ]
    """<p>A unique identifier assigned to this record within the shard, used for ordering and tracking purposes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Record) -> dict:
    out: dict = {}
    if "event_version" in value:
        out["eventVersion"] = value["event_version"]
    if "created_at" in value:
        import capo_keyspacesstreams.types.date

        out["createdAt"] = capo_keyspacesstreams.types.date.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "origin" in value:
        import capo_keyspacesstreams.types.origin_type

        out["origin"] = capo_keyspacesstreams.types.origin_type.serialize_aws_json_1_0(
            value["origin"]
        )
    if "partition_keys" in value:
        import capo_keyspacesstreams.types.keyspaces_keys_map

        out["partitionKeys"] = (
            capo_keyspacesstreams.types.keyspaces_keys_map.serialize_aws_json_1_0(
                value["partition_keys"]
            )
        )
    if "clustering_keys" in value:
        import capo_keyspacesstreams.types.keyspaces_keys_map

        out["clusteringKeys"] = (
            capo_keyspacesstreams.types.keyspaces_keys_map.serialize_aws_json_1_0(
                value["clustering_keys"]
            )
        )
    if "new_image" in value:
        import capo_keyspacesstreams.types.keyspaces_row

        out["newImage"] = (
            capo_keyspacesstreams.types.keyspaces_row.serialize_aws_json_1_0(
                value["new_image"]
            )
        )
    if "old_image" in value:
        import capo_keyspacesstreams.types.keyspaces_row

        out["oldImage"] = (
            capo_keyspacesstreams.types.keyspaces_row.serialize_aws_json_1_0(
                value["old_image"]
            )
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "eventVersion" in data:
        out["event_version"] = data["eventVersion"]
    if "createdAt" in data:
        import capo_keyspacesstreams.types.date

        out["created_at"] = capo_keyspacesstreams.types.date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    if "origin" in data:
        import capo_keyspacesstreams.types.origin_type

        out["origin"] = (
            capo_keyspacesstreams.types.origin_type.deserialize_aws_json_1_0(
                data["origin"]
            )
        )
    if "partitionKeys" in data:
        import capo_keyspacesstreams.types.keyspaces_keys_map

        out["partition_keys"] = (
            capo_keyspacesstreams.types.keyspaces_keys_map.deserialize_aws_json_1_0(
                data["partitionKeys"]
            )
        )
    if "clusteringKeys" in data:
        import capo_keyspacesstreams.types.keyspaces_keys_map

        out["clustering_keys"] = (
            capo_keyspacesstreams.types.keyspaces_keys_map.deserialize_aws_json_1_0(
                data["clusteringKeys"]
            )
        )
    if "newImage" in data:
        import capo_keyspacesstreams.types.keyspaces_row

        out["new_image"] = (
            capo_keyspacesstreams.types.keyspaces_row.deserialize_aws_json_1_0(
                data["newImage"]
            )
        )
    if "oldImage" in data:
        import capo_keyspacesstreams.types.keyspaces_row

        out["old_image"] = (
            capo_keyspacesstreams.types.keyspaces_row.deserialize_aws_json_1_0(
                data["oldImage"]
            )
        )
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out
