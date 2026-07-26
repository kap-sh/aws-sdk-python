"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetSignalCatalogResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.node_counts
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.timestamp


class GetSignalCatalogResponse(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog. </p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the signal catalog. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the signal catalog. </p>"""
    node_counts: NotRequired["capo_iotfleetwise.types.node_counts.NodeCounts"]
    """<p> The total number of network nodes specified in a signal catalog. </p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The last time the signal catalog was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSignalCatalogResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "node_counts" in value:
        import capo_iotfleetwise.types.node_counts

        out["nodeCounts"] = capo_iotfleetwise.types.node_counts.serialize_aws_json_1_0(
            value["node_counts"]
        )
    import capo_iotfleetwise.types.timestamp

    out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import capo_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSignalCatalogResponse:
    out: GetSignalCatalogResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetSignalCatalogResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSignalCatalogResponse.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "nodeCounts" in data:
        import capo_iotfleetwise.types.node_counts

        out["node_counts"] = (
            capo_iotfleetwise.types.node_counts.deserialize_aws_json_1_0(
                data["nodeCounts"]
            )
        )
    if "creationTime" in data:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("GetSignalCatalogResponse.creation_time required")
    if "lastModificationTime" in data:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetSignalCatalogResponse.last_modification_time required"
        )
    return out
