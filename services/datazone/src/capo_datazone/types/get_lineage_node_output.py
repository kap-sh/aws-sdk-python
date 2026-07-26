"""Generated from Smithy shape ``com.amazonaws.datazone#GetLineageNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_output_list
    import capo_datazone.types.lineage_node_id
    import capo_datazone.types.lineage_node_reference_list
    import capo_datazone.types.revision
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GetLineageNodeOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you're getting the data lineage node.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data lineage node.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data lineage node.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data lineage node was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data lineage node.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the data lineage node was updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the data lineage node.</p>"""
    id: "capo_datazone.types.lineage_node_id.LineageNodeId"
    """<p>The ID of the data lineage node.</p>"""
    type_name: "str"
    """<p>The name of the type of the specified data lineage node.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision type of the specified data lineage node.</p>"""
    source_identifier: NotRequired["str"]
    """<p>The source identifier of the data lineage node.</p>"""
    event_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of the event described in the data lineage node.</p>"""
    forms_output: NotRequired["capo_datazone.types.form_output_list.FormOutputList"]
    """<p>The metadata of the specified data lineage node.</p>"""
    upstream_nodes: NotRequired[
        "capo_datazone.types.lineage_node_reference_list.LineageNodeReferenceList"
    ]
    """<p>The upstream nodes of the specified data lineage node.</p>"""
    downstream_nodes: NotRequired[
        "capo_datazone.types.lineage_node_reference_list.LineageNodeReferenceList"
    ]
    """<p>The downsteam nodes of the specified data lineage node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLineageNodeOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["id"] = value["id"]
    out["typeName"] = value["type_name"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "source_identifier" in value:
        out["sourceIdentifier"] = value["source_identifier"]
    if "event_timestamp" in value:
        import capo_datazone.types._prelude.timestamp

        out["eventTimestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["event_timestamp"]
        )
    if "forms_output" in value:
        import capo_datazone.types.form_output_list

        out["formsOutput"] = capo_datazone.types.form_output_list.serialize_json(
            value["forms_output"]
        )
    if "upstream_nodes" in value:
        import capo_datazone.types.lineage_node_reference_list

        out["upstreamNodes"] = (
            capo_datazone.types.lineage_node_reference_list.serialize_json(
                value["upstream_nodes"]
            )
        )
    if "downstream_nodes" in value:
        import capo_datazone.types.lineage_node_reference_list

        out["downstreamNodes"] = (
            capo_datazone.types.lineage_node_reference_list.serialize_json(
                value["downstream_nodes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLineageNodeOutput:
    out: GetLineageNodeOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetLineageNodeOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetLineageNodeOutput.id required")
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    else:
        raise DeserializationError("GetLineageNodeOutput.type_name required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "sourceIdentifier" in data:
        out["source_identifier"] = data["sourceIdentifier"]
    if "eventTimestamp" in data:
        import capo_datazone.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    if "formsOutput" in data:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.deserialize_json(
            data["formsOutput"]
        )
    if "upstreamNodes" in data:
        import capo_datazone.types.lineage_node_reference_list

        out["upstream_nodes"] = (
            capo_datazone.types.lineage_node_reference_list.deserialize_json(
                data["upstreamNodes"]
            )
        )
    if "downstreamNodes" in data:
        import capo_datazone.types.lineage_node_reference_list

        out["downstream_nodes"] = (
            capo_datazone.types.lineage_node_reference_list.deserialize_json(
                data["downstreamNodes"]
            )
        )
    return out
