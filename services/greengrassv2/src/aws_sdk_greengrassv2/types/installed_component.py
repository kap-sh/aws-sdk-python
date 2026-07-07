"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_name_string
    import aws_sdk_greengrassv2.types.component_version_string
    import aws_sdk_greengrassv2.types.installed_component_lifecycle_state
    import aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code_list
    import aws_sdk_greengrassv2.types.is_root
    import aws_sdk_greengrassv2.types.lifecycle_state_details
    import aws_sdk_greengrassv2.types.non_empty_string
    import aws_sdk_greengrassv2.types.timestamp


class InstalledComponent(TypedDict, closed=True):
    component_name: NotRequired[
        "aws_sdk_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    lifecycle_state: NotRequired[
        "aws_sdk_greengrassv2.types.installed_component_lifecycle_state.InstalledComponentLifecycleState"
    ]
    """<p>The lifecycle state of the component.</p>"""
    lifecycle_state_details: NotRequired[
        "aws_sdk_greengrassv2.types.lifecycle_state_details.LifecycleStateDetails"
    ]
    """<p>A detailed response about the lifecycle state of the component that explains the reason why a component has an error or is broken.</p>"""
    is_root: "aws_sdk_greengrassv2.types.is_root.IsRoot"
    """<p>Whether or not the component is a root component.</p>"""
    last_status_change_timestamp: NotRequired[
        "aws_sdk_greengrassv2.types.timestamp.Timestamp"
    ]
    """<p>The status of how current the data is.</p> <p>This response is based off of component state changes. The status reflects component disruptions and deployments. If a component only sees a configuration update during a deployment, it might not undergo a state change and this status would not be updated.</p>"""
    last_reported_timestamp: NotRequired[
        "aws_sdk_greengrassv2.types.timestamp.Timestamp"
    ]
    """<p>The last time the Greengrass core device sent a message containing a component's state to the Amazon Web Services Cloud.</p> <p>A component does not need to see a state change for this field to update.</p>"""
    last_installation_source: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The most recent deployment source that brought the component to the Greengrass core device. For a thing group deployment or thing deployment, the source will be the ID of the last deployment that contained the component. For local deployments it will be <code>LOCAL</code>.</p> <note> <p>Any deployment will attempt to reinstall currently broken components on the device, which will update the last installation source.</p> </note>"""
    lifecycle_status_codes: NotRequired[
        "aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code_list.InstalledComponentLifecycleStatusCodeList"
    ]
    """<p>The status codes that indicate the reason for failure whenever the <code>lifecycleState</code> has an error or is in a broken state.</p> <note> <p>Greengrass nucleus v2.8.0 or later is required to get an accurate <code>lifecycleStatusCodes</code> response. This response can be inaccurate in earlier Greengrass nucleus versions.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstalledComponent) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "lifecycle_state" in value:
        import aws_sdk_greengrassv2.types.installed_component_lifecycle_state

        out["lifecycleState"] = (
            aws_sdk_greengrassv2.types.installed_component_lifecycle_state.serialize_json(
                value["lifecycle_state"]
            )
        )
    if "lifecycle_state_details" in value:
        out["lifecycleStateDetails"] = value["lifecycle_state_details"]
    out["isRoot"] = value.get("is_root", False)
    if "last_status_change_timestamp" in value:
        import aws_sdk_greengrassv2.types.timestamp

        out["lastStatusChangeTimestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.serialize_json(
                value["last_status_change_timestamp"]
            )
        )
    if "last_reported_timestamp" in value:
        import aws_sdk_greengrassv2.types.timestamp

        out["lastReportedTimestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.serialize_json(
                value["last_reported_timestamp"]
            )
        )
    if "last_installation_source" in value:
        out["lastInstallationSource"] = value["last_installation_source"]
    if "lifecycle_status_codes" in value:
        import aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code_list

        out["lifecycleStatusCodes"] = (
            aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code_list.serialize_json(
                value["lifecycle_status_codes"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstalledComponent:
    out: InstalledComponent = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentVersion" in data:
        out["component_version"] = data["componentVersion"]
    if "lifecycleState" in data:
        import aws_sdk_greengrassv2.types.installed_component_lifecycle_state

        out["lifecycle_state"] = (
            aws_sdk_greengrassv2.types.installed_component_lifecycle_state.deserialize_json(
                data["lifecycleState"]
            )
        )
    if "lifecycleStateDetails" in data:
        out["lifecycle_state_details"] = data["lifecycleStateDetails"]
    if "isRoot" in data:
        out["is_root"] = data["isRoot"]
    else:
        out["is_root"] = False
    if "lastStatusChangeTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["last_status_change_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["lastStatusChangeTimestamp"]
            )
        )
    if "lastReportedTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["last_reported_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["lastReportedTimestamp"]
            )
        )
    if "lastInstallationSource" in data:
        out["last_installation_source"] = data["lastInstallationSource"]
    if "lifecycleStatusCodes" in data:
        import aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code_list

        out["lifecycle_status_codes"] = (
            aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code_list.deserialize_json(
                data["lifecycleStatusCodes"]
            )
        )
    return out
