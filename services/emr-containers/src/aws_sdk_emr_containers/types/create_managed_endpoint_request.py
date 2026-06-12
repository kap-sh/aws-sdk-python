"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateManagedEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.acm_cert_arn
    import aws_sdk_emr_containers.types.client_token
    import aws_sdk_emr_containers.types.configuration_overrides
    import aws_sdk_emr_containers.types.endpoint_type
    import aws_sdk_emr_containers.types.iam_role_arn
    import aws_sdk_emr_containers.types.release_label
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.tag_map


class CreateManagedEndpointRequest(TypedDict):
    name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The name of the managed endpoint.</p>"""
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The ID of the virtual cluster for which a managed endpoint is created.</p>"""
    type: "aws_sdk_emr_containers.types.endpoint_type.EndpointType"
    """<p>The type of the managed endpoint.</p>"""
    release_label: "aws_sdk_emr_containers.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release version.</p>"""
    execution_role_arn: "aws_sdk_emr_containers.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the execution role.</p>"""
    certificate_arn: NotRequired["aws_sdk_emr_containers.types.acm_cert_arn.ACMCertArn"]
    """<p>The certificate ARN provided by users for the managed endpoint. This field is under deprecation and will be removed in future releases.</p>"""
    configuration_overrides: NotRequired[
        "aws_sdk_emr_containers.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration settings that will be used to override existing configurations.</p>"""
    client_token: "aws_sdk_emr_containers.types.client_token.ClientToken"
    """<p>The client idempotency token for this create call.</p>"""
    tags: NotRequired["aws_sdk_emr_containers.types.tag_map.TagMap"]
    """<p>The tags of the managed endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateManagedEndpointRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["releaseLabel"] = value["release_label"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "configuration_overrides" in value:
        import aws_sdk_emr_containers.types.configuration_overrides

        out["configurationOverrides"] = (
            aws_sdk_emr_containers.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateManagedEndpointRequest:
    out: CreateManagedEndpointRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateManagedEndpointRequest.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateManagedEndpointRequest.type required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError(
            "CreateManagedEndpointRequest.release_label required"
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "CreateManagedEndpointRequest.execution_role_arn required"
        )
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "configurationOverrides" in data:
        import aws_sdk_emr_containers.types.configuration_overrides

        out["configuration_overrides"] = (
            aws_sdk_emr_containers.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateManagedEndpointRequest.client_token required")
    if "tags" in data:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
