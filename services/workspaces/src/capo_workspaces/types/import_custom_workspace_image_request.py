"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportCustomWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.custom_image_protocol
    import capo_workspaces.types.image_compute_type
    import capo_workspaces.types.image_source_identifier
    import capo_workspaces.types.infrastructure_configuration_arn
    import capo_workspaces.types.os_version
    import capo_workspaces.types.platform
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.workspace_image_description
    import capo_workspaces.types.workspace_image_name


class ImportCustomWorkspaceImageRequest(TypedDict, closed=True):
    image_name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the WorkSpace image.</p>"""
    image_description: (
        "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    )
    """<p>The description of the WorkSpace image.</p>"""
    compute_type: "capo_workspaces.types.image_compute_type.ImageComputeType"
    """<p>The supported compute type for the WorkSpace image.</p>"""
    protocol: "capo_workspaces.types.custom_image_protocol.CustomImageProtocol"
    """<p>The supported protocol for the WorkSpace image. Windows 11 does not support PCOIP protocol.</p>"""
    image_source: "capo_workspaces.types.image_source_identifier.ImageSourceIdentifier"
    """<p>The options for image import source.</p>"""
    infrastructure_configuration_arn: "capo_workspaces.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The infrastructure configuration ARN that specifies how the WorkSpace image is built.</p>"""
    platform: "capo_workspaces.types.platform.Platform"
    """<p>The platform for the WorkSpace image source.</p>"""
    os_version: "capo_workspaces.types.os_version.OSVersion"
    """<p>The OS version for the WorkSpace image source.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The resource tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCustomWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["ImageName"] = value["image_name"]
    out["ImageDescription"] = value["image_description"]
    import capo_workspaces.types.image_compute_type

    out["ComputeType"] = (
        capo_workspaces.types.image_compute_type.serialize_aws_json_1_1(
            value["compute_type"]
        )
    )
    import capo_workspaces.types.custom_image_protocol

    out["Protocol"] = (
        capo_workspaces.types.custom_image_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    )
    import capo_workspaces.types.image_source_identifier

    out["ImageSource"] = (
        capo_workspaces.types.image_source_identifier.serialize_aws_json_1_1(
            value["image_source"]
        )
    )
    out["InfrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    import capo_workspaces.types.platform

    out["Platform"] = capo_workspaces.types.platform.serialize_aws_json_1_1(
        value["platform"]
    )
    import capo_workspaces.types.os_version

    out["OsVersion"] = capo_workspaces.types.os_version.serialize_aws_json_1_1(
        value["os_version"]
    )
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCustomWorkspaceImageRequest:
    out: ImportCustomWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.image_name required"
        )
    if "ImageDescription" in data:
        out["image_description"] = data["ImageDescription"]
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.image_description required"
        )
    if "ComputeType" in data:
        import capo_workspaces.types.image_compute_type

        out["compute_type"] = (
            capo_workspaces.types.image_compute_type.deserialize_aws_json_1_1(
                data["ComputeType"]
            )
        )
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.compute_type required"
        )
    if "Protocol" in data:
        import capo_workspaces.types.custom_image_protocol

        out["protocol"] = (
            capo_workspaces.types.custom_image_protocol.deserialize_aws_json_1_1(
                data["Protocol"]
            )
        )
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.protocol required"
        )
    if "ImageSource" in data:
        import capo_workspaces.types.image_source_identifier

        out["image_source"] = (
            capo_workspaces.types.image_source_identifier.deserialize_aws_json_1_1(
                data["ImageSource"]
            )
        )
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.image_source required"
        )
    if "InfrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["InfrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.infrastructure_configuration_arn required"
        )
    if "Platform" in data:
        import capo_workspaces.types.platform

        out["platform"] = capo_workspaces.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.platform required"
        )
    if "OsVersion" in data:
        import capo_workspaces.types.os_version

        out["os_version"] = capo_workspaces.types.os_version.deserialize_aws_json_1_1(
            data["OsVersion"]
        )
    else:
        raise DeserializationError(
            "ImportCustomWorkspaceImageRequest.os_version required"
        )
    if "Tags" in data:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
