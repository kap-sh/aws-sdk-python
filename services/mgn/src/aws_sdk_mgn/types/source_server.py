"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.application_id
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.data_replication_info
    import aws_sdk_mgn.types.launched_instance
    import aws_sdk_mgn.types.life_cycle
    import aws_sdk_mgn.types.replication_type
    import aws_sdk_mgn.types.source_properties
    import aws_sdk_mgn.types.source_server_connector_action
    import aws_sdk_mgn.types.source_server_id
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.user_provided_id
    import aws_sdk_mgn.types.vcenter_client_id


class SourceServer(TypedDict, closed=True):
    source_server_id: NotRequired["aws_sdk_mgn.types.source_server_id.SourceServerID"]
    """<p>Source server ID.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Source server ARN.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Source server archived status.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Source server Tags.</p>"""
    launched_instance: NotRequired[
        "aws_sdk_mgn.types.launched_instance.LaunchedInstance"
    ]
    """<p>Source server launched instance.</p>"""
    data_replication_info: NotRequired[
        "aws_sdk_mgn.types.data_replication_info.DataReplicationInfo"
    ]
    """<p>Source server data replication info.</p>"""
    life_cycle: NotRequired["aws_sdk_mgn.types.life_cycle.LifeCycle"]
    """<p>Source server lifecycle state.</p>"""
    source_properties: NotRequired[
        "aws_sdk_mgn.types.source_properties.SourceProperties"
    ]
    """<p>Source server properties.</p>"""
    replication_type: NotRequired["aws_sdk_mgn.types.replication_type.ReplicationType"]
    """<p>Source server replication type.</p>"""
    vcenter_client_id: NotRequired[
        "aws_sdk_mgn.types.vcenter_client_id.VcenterClientID"
    ]
    """<p>Source server vCenter client id.</p>"""
    application_id: NotRequired["aws_sdk_mgn.types.application_id.ApplicationID"]
    """<p>Source server application ID.</p>"""
    user_provided_id: NotRequired["aws_sdk_mgn.types.user_provided_id.UserProvidedId"]
    """<p>Source server user provided ID.</p>"""
    fqdn_for_action_framework: NotRequired[
        "aws_sdk_mgn.types.bounded_string.BoundedString"
    ]
    """<p>Source server fqdn for action framework.</p>"""
    connector_action: NotRequired[
        "aws_sdk_mgn.types.source_server_connector_action.SourceServerConnectorAction"
    ]
    """<p>Source Server connector action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceServer) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "launched_instance" in value:
        import aws_sdk_mgn.types.launched_instance

        out["launchedInstance"] = aws_sdk_mgn.types.launched_instance.serialize_json(
            value["launched_instance"]
        )
    if "data_replication_info" in value:
        import aws_sdk_mgn.types.data_replication_info

        out["dataReplicationInfo"] = (
            aws_sdk_mgn.types.data_replication_info.serialize_json(
                value["data_replication_info"]
            )
        )
    if "life_cycle" in value:
        import aws_sdk_mgn.types.life_cycle

        out["lifeCycle"] = aws_sdk_mgn.types.life_cycle.serialize_json(
            value["life_cycle"]
        )
    if "source_properties" in value:
        import aws_sdk_mgn.types.source_properties

        out["sourceProperties"] = aws_sdk_mgn.types.source_properties.serialize_json(
            value["source_properties"]
        )
    if "replication_type" in value:
        out["replicationType"] = value["replication_type"]
    if "vcenter_client_id" in value:
        out["vcenterClientID"] = value["vcenter_client_id"]
    if "application_id" in value:
        out["applicationID"] = value["application_id"]
    if "user_provided_id" in value:
        out["userProvidedID"] = value["user_provided_id"]
    if "fqdn_for_action_framework" in value:
        out["fqdnForActionFramework"] = value["fqdn_for_action_framework"]
    if "connector_action" in value:
        import aws_sdk_mgn.types.source_server_connector_action

        out["connectorAction"] = (
            aws_sdk_mgn.types.source_server_connector_action.serialize_json(
                value["connector_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceServer:
    out: SourceServer = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "isArchived" in data:
        out["is_archived"] = data["isArchived"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "launchedInstance" in data:
        import aws_sdk_mgn.types.launched_instance

        out["launched_instance"] = aws_sdk_mgn.types.launched_instance.deserialize_json(
            data["launchedInstance"]
        )
    if "dataReplicationInfo" in data:
        import aws_sdk_mgn.types.data_replication_info

        out["data_replication_info"] = (
            aws_sdk_mgn.types.data_replication_info.deserialize_json(
                data["dataReplicationInfo"]
            )
        )
    if "lifeCycle" in data:
        import aws_sdk_mgn.types.life_cycle

        out["life_cycle"] = aws_sdk_mgn.types.life_cycle.deserialize_json(
            data["lifeCycle"]
        )
    if "sourceProperties" in data:
        import aws_sdk_mgn.types.source_properties

        out["source_properties"] = aws_sdk_mgn.types.source_properties.deserialize_json(
            data["sourceProperties"]
        )
    if "replicationType" in data:
        out["replication_type"] = data["replicationType"]
    if "vcenterClientID" in data:
        out["vcenter_client_id"] = data["vcenterClientID"]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    if "userProvidedID" in data:
        out["user_provided_id"] = data["userProvidedID"]
    if "fqdnForActionFramework" in data:
        out["fqdn_for_action_framework"] = data["fqdnForActionFramework"]
    if "connectorAction" in data:
        import aws_sdk_mgn.types.source_server_connector_action

        out["connector_action"] = (
            aws_sdk_mgn.types.source_server_connector_action.deserialize_json(
                data["connectorAction"]
            )
        )
    return out
