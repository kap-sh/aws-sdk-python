"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeCustomPluginResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601
    import capo_kafkaconnect.types.custom_plugin_revision_summary
    import capo_kafkaconnect.types.custom_plugin_state
    import capo_kafkaconnect.types.state_description


class DescribeCustomPluginResponse(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the custom plugin was created.</p>"""
    custom_plugin_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom plugin.</p>"""
    custom_plugin_state: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_state.CustomPluginState"
    ]
    """<p>The state of the custom plugin.</p>"""
    description: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The description of the custom plugin.</p>"""
    latest_revision: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_revision_summary.CustomPluginRevisionSummary"
    ]
    """<p>The latest successfully created revision of the custom plugin. If there are no successfully created revisions, this field will be absent.</p>"""
    name: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The name of the custom plugin.</p>"""
    state_description: NotRequired[
        "capo_kafkaconnect.types.state_description.StateDescription"
    ]
    """<p>Details about the state of a custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomPluginResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "custom_plugin_arn" in value:
        out["customPluginArn"] = value["custom_plugin_arn"]
    if "custom_plugin_state" in value:
        out["customPluginState"] = value["custom_plugin_state"]
    if "description" in value:
        out["description"] = value["description"]
    if "latest_revision" in value:
        import capo_kafkaconnect.types.custom_plugin_revision_summary

        out["latestRevision"] = (
            capo_kafkaconnect.types.custom_plugin_revision_summary.serialize_json(
                value["latest_revision"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "state_description" in value:
        import capo_kafkaconnect.types.state_description

        out["stateDescription"] = (
            capo_kafkaconnect.types.state_description.serialize_json(
                value["state_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeCustomPluginResponse:
    out: DescribeCustomPluginResponse = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "customPluginArn" in data:
        out["custom_plugin_arn"] = data["customPluginArn"]
    if "customPluginState" in data:
        out["custom_plugin_state"] = data["customPluginState"]
    if "description" in data:
        out["description"] = data["description"]
    if "latestRevision" in data:
        import capo_kafkaconnect.types.custom_plugin_revision_summary

        out["latest_revision"] = (
            capo_kafkaconnect.types.custom_plugin_revision_summary.deserialize_json(
                data["latestRevision"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "stateDescription" in data:
        import capo_kafkaconnect.types.state_description

        out["state_description"] = (
            capo_kafkaconnect.types.state_description.deserialize_json(
                data["stateDescription"]
            )
        )
    return out
