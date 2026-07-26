"""Generated from Smithy shape ``com.amazonaws.ssmsap#RegisterApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.application_credential_list
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.application_type
    import capo_ssm_sap.types.component_info_list
    import capo_ssm_sap.types.instance_list
    import capo_ssm_sap.types.sap_instance_number
    import capo_ssm_sap.types.sid
    import capo_ssm_sap.types.ssm_sap_arn
    import capo_ssm_sap.types.tag_map


class RegisterApplicationInput(TypedDict, closed=True):
    application_id: "capo_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    application_type: "capo_ssm_sap.types.application_type.ApplicationType"
    """<p>The type of the application.</p>"""
    instances: "capo_ssm_sap.types.instance_list.InstanceList"
    """<p>The Amazon EC2 instances on which your SAP application is running.</p>"""
    sap_instance_number: NotRequired[
        "capo_ssm_sap.types.sap_instance_number.SAPInstanceNumber"
    ]
    """<p>The SAP instance number of the application.</p>"""
    sid: NotRequired["capo_ssm_sap.types.sid.SID"]
    """<p>The System ID of the application.</p>"""
    tags: NotRequired["capo_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags to be attached to the SAP application.</p>"""
    credentials: (
        "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
    )
    """<p>The credentials of the SAP application.</p>"""
    database_arn: NotRequired["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name of the SAP HANA database.</p>"""
    components_info: NotRequired[
        "capo_ssm_sap.types.component_info_list.ComponentInfoList"
    ]
    """<p>This is an optional parameter for component details to which the SAP ABAP application is attached, such as Web Dispatcher.</p> <p>This is an array of ApplicationComponent objects. You may input 0 to 5 items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterApplicationInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    import capo_ssm_sap.types.application_type

    out["ApplicationType"] = capo_ssm_sap.types.application_type.serialize_json(
        value["application_type"]
    )
    import capo_ssm_sap.types.instance_list

    out["Instances"] = capo_ssm_sap.types.instance_list.serialize_json(
        value["instances"]
    )
    if "sap_instance_number" in value:
        out["SapInstanceNumber"] = value["sap_instance_number"]
    if "sid" in value:
        out["Sid"] = value["sid"]
    if "tags" in value:
        import capo_ssm_sap.types.tag_map

        out["Tags"] = capo_ssm_sap.types.tag_map.serialize_json(value["tags"])
    import capo_ssm_sap.types.application_credential_list

    out["Credentials"] = capo_ssm_sap.types.application_credential_list.serialize_json(
        value.get("credentials", [])
    )
    if "database_arn" in value:
        out["DatabaseArn"] = value["database_arn"]
    if "components_info" in value:
        import capo_ssm_sap.types.component_info_list

        out["ComponentsInfo"] = capo_ssm_sap.types.component_info_list.serialize_json(
            value["components_info"]
        )
    return out


def deserialize_json(data: dict) -> RegisterApplicationInput:
    out: RegisterApplicationInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError("RegisterApplicationInput.application_id required")
    if "ApplicationType" in data:
        import capo_ssm_sap.types.application_type

        out["application_type"] = capo_ssm_sap.types.application_type.deserialize_json(
            data["ApplicationType"]
        )
    else:
        raise DeserializationError("RegisterApplicationInput.application_type required")
    if "Instances" in data:
        import capo_ssm_sap.types.instance_list

        out["instances"] = capo_ssm_sap.types.instance_list.deserialize_json(
            data["Instances"]
        )
    else:
        raise DeserializationError("RegisterApplicationInput.instances required")
    if "SapInstanceNumber" in data:
        out["sap_instance_number"] = data["SapInstanceNumber"]
    if "Sid" in data:
        out["sid"] = data["Sid"]
    if "Tags" in data:
        import capo_ssm_sap.types.tag_map

        out["tags"] = capo_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    if "Credentials" in data:
        import capo_ssm_sap.types.application_credential_list

        out["credentials"] = (
            capo_ssm_sap.types.application_credential_list.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        out["credentials"] = []
    if "DatabaseArn" in data:
        out["database_arn"] = data["DatabaseArn"]
    if "ComponentsInfo" in data:
        import capo_ssm_sap.types.component_info_list

        out["components_info"] = (
            capo_ssm_sap.types.component_info_list.deserialize_json(
                data["ComponentsInfo"]
            )
        )
    return out
