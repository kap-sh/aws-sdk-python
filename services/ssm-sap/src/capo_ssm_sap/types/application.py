"""Generated from Smithy shape ``com.amazonaws.ssmsap#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_sap.types.app_registry_arn
    import capo_ssm_sap.types.application_arn_list
    import capo_ssm_sap.types.application_discovery_status
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.application_status
    import capo_ssm_sap.types.application_type
    import capo_ssm_sap.types.component_id_list
    import capo_ssm_sap.types.ssm_sap_arn


class Application(TypedDict, closed=True):
    id: NotRequired["capo_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    type: NotRequired["capo_ssm_sap.types.application_type.ApplicationType"]
    """<p>The type of the application.</p>"""
    arn: NotRequired["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    app_registry_arn: NotRequired["capo_ssm_sap.types.app_registry_arn.AppRegistryArn"]
    """<p>The Amazon Resource Name (ARN) of the Application Registry.</p>"""
    status: NotRequired["capo_ssm_sap.types.application_status.ApplicationStatus"]
    """<p>The status of the application.</p>"""
    discovery_status: NotRequired[
        "capo_ssm_sap.types.application_discovery_status.ApplicationDiscoveryStatus"
    ]
    """<p>The latest discovery result for the application.</p>"""
    components: NotRequired["capo_ssm_sap.types.component_id_list.ComponentIdList"]
    """<p>The components of the application.</p>"""
    last_updated: NotRequired["datetime.datetime"]
    """<p>The time at which the application was last updated.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message.</p>"""
    associated_application_arns: NotRequired[
        "capo_ssm_sap.types.application_arn_list.ApplicationArnList"
    ]
    """<p>The Amazon Resource Names of the associated AWS Systems Manager for SAP applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_ssm_sap.types.application_type

        out["Type"] = capo_ssm_sap.types.application_type.serialize_json(value["type"])
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "app_registry_arn" in value:
        out["AppRegistryArn"] = value["app_registry_arn"]
    if "status" in value:
        import capo_ssm_sap.types.application_status

        out["Status"] = capo_ssm_sap.types.application_status.serialize_json(
            value["status"]
        )
    if "discovery_status" in value:
        import capo_ssm_sap.types.application_discovery_status

        out["DiscoveryStatus"] = (
            capo_ssm_sap.types.application_discovery_status.serialize_json(
                value["discovery_status"]
            )
        )
    if "components" in value:
        import capo_ssm_sap.types.component_id_list

        out["Components"] = capo_ssm_sap.types.component_id_list.serialize_json(
            value["components"]
        )
    if "last_updated" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["LastUpdated"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["last_updated"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "associated_application_arns" in value:
        import capo_ssm_sap.types.application_arn_list

        out["AssociatedApplicationArns"] = (
            capo_ssm_sap.types.application_arn_list.serialize_json(
                value["associated_application_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import capo_ssm_sap.types.application_type

        out["type"] = capo_ssm_sap.types.application_type.deserialize_json(data["Type"])
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AppRegistryArn" in data:
        out["app_registry_arn"] = data["AppRegistryArn"]
    if "Status" in data:
        import capo_ssm_sap.types.application_status

        out["status"] = capo_ssm_sap.types.application_status.deserialize_json(
            data["Status"]
        )
    if "DiscoveryStatus" in data:
        import capo_ssm_sap.types.application_discovery_status

        out["discovery_status"] = (
            capo_ssm_sap.types.application_discovery_status.deserialize_json(
                data["DiscoveryStatus"]
            )
        )
    if "Components" in data:
        import capo_ssm_sap.types.component_id_list

        out["components"] = capo_ssm_sap.types.component_id_list.deserialize_json(
            data["Components"]
        )
    if "LastUpdated" in data:
        import capo_ssm_sap.types._prelude.timestamp

        out["last_updated"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["LastUpdated"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "AssociatedApplicationArns" in data:
        import capo_ssm_sap.types.application_arn_list

        out["associated_application_arns"] = (
            capo_ssm_sap.types.application_arn_list.deserialize_json(
                data["AssociatedApplicationArns"]
            )
        )
    return out
